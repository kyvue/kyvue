import docker # type: ignore

class DockerPlugin:
    def __init__(self):
        self.client = docker.from_env()

    def collect_data(self):
        """
        Collect Docker information including containers, images, volumes, and networks.
        """
        try:
            data = {
                "containers": self._get_containers(),
                "images": self._get_images(),
                "volumes": self._get_volumes(),
                "networks": self._get_networks(),
            }
            return data
        except Exception as e:
            return {"error": str(e)}

    def _get_containers(self):
        containers = []
        for container in self.client.containers.list():
            containers.append({
                "id": container.id,
                "name": container.name,
                "status": container.status,
                "image": container.image.tags,
                "created": container.attrs.get("Created"),
                "ports": container.attrs.get("NetworkSettings", {}).get("Ports"),
            })
        return containers

    def _get_images(self):
        images = []
        for image in self.client.images.list():
            images.append({
                "id": image.id,
                "tags": image.tags,
                "created": image.attrs.get("Created"),
                "size": image.attrs.get("Size"),
            })
        return images

    def _get_volumes(self):
        volumes = []
        for volume in self.client.volumes.list():
            volumes.append({
                "name": volume.name,
                "mountpoint": volume.attrs.get("Mountpoint"),
                "size": volume.attrs.get("UsageData", {}).get("Size", "Unknown"),
            })
        return volumes

    def _get_networks(self):
        networks = []
        for network in self.client.networks.list():
            networks.append({
                "name": network.name,
                "id": network.id,
                "containers": network.attrs.get("Containers"),
            })
        return networks
