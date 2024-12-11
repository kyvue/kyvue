


class DockerSerializer:
    @staticmethod
    def serialize(data):
        """
        Serialize Docker data into a clean format.
        """
        if "error" in data:
            return {"status": "error", "message": data["error"]}
        
        return {
            "status": "success",
            "data": {
                "containers": data["containers"],
                "images": data["images"],
                "volumes": data["volumes"],
                "networks": data["networks"],
            },
        }
