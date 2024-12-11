import psutil
import platform
from datetime import datetime

class SystemPlugin:
    """
    A plugin to collect system metrics like RAM usage, disk usage, CPU usage, system uptime, and OS information.
    """

    @staticmethod
    def collect_data():
        system_info = {
            "ram_usage": SystemPlugin.get_ram_usage(),
            "disk_usage": SystemPlugin.get_disk_usage(),
            "uptime": SystemPlugin.get_uptime(),
            "cpu_usage": SystemPlugin.get_cpu_usage(),
            "system_info": SystemPlugin.get_system_info()
        }
        return system_info

    @staticmethod
    def get_ram_usage():
        """
        Returns RAM usage information including used and free percentages.
        """
        total = psutil.virtual_memory().total
        used = psutil.virtual_memory().used
        free = psutil.virtual_memory().free
        percent = psutil.virtual_memory().percent

        # Calculating free percentage
        free_percentage = 100 - percent
        
        return {
            "total": total,
            "used": used,
            "free": free,
            "percent": percent,
            "used_percentage": percent,  # Same as percent
            "free_percentage": free_percentage
        }

    @staticmethod
    def get_disk_usage():
        """
        Returns disk usage information including used and free percentages.
        """
        disk = psutil.disk_usage('/')
        used_percentage = disk.percent
        free_percentage = 100 - used_percentage
        
        return {
            "total": disk.total,
            "used": disk.used,
            "free": disk.free,
            "percent": used_percentage,
            "used_percentage": used_percentage,
            "free_percentage": free_percentage
        }

    @staticmethod
    def get_uptime():
        """
        Returns system uptime since last reboot.
        """
        uptime_seconds = psutil.boot_time()
        uptime = datetime.fromtimestamp(uptime_seconds)
        return {
            "last_reboot": uptime.strftime('%Y-%m-%d %H:%M:%S'),
            "uptime_seconds": uptime_seconds
        }

    @staticmethod
    def get_cpu_usage():
        """
        Returns the current CPU usage.
        """
        cpu_percent = psutil.cpu_percent(interval=1)
        return {
            "cpu_percent": cpu_percent
        }

    @staticmethod
    def get_system_info():
        """
        Returns system information like OS and version.
        """
        system_info = {
            "os": platform.system(),
            "os_version": platform.version(),
            "architecture": platform.architecture()[0]
        }
        return system_info
