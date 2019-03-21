"""
This Scrit gives CPU Utilization %

__PLATFORM = Linux, Unix
__PTYHON_VERSION = 2.7 +
__Author = MockArch
__Github = https://github.com/MockArch
"""
import subprocess


class CpuMeta(object):
    """
    """
    __LOCATION_FILE = '/proc/stat'

    def __init__(self):
        self.location_of_file = __class__.__LOCATION_FILE
        self.proc_file_content = None
        self.cpu_data = []
        self.number_of_cpu = 0
        """
        self.total_cpu_time_since_boot = None
        self.total_cpu_idle_time_since_boot = None
        self.total_cpu_usage_time_since_boot = None 
        self.total_cpu_percentage = None
        """

    def get_cpu_usage_percentage(self):
        """
        """
        self._get_cpu_data()
        self.calculate_number_of_cpu()
        

    def _get_cpu_data(self):
        try:
            data = subprocess.Popen(["cat", "/proc/stat"], stdout=subprocess.PIPE)
            data = data.communicate()
            for cpus in data:
                if "cpu" in cpus:
                    self.cpu_data.append(cpus)
        except Exception as e:
            print(e)   
    
    def calculate_number_of_cpu(self):
        self.number_of_cpu = len(self.cpu_data) - 1




        




if __name__ == "__main__":
    obj = CpuMeta()
    obj.get_cpu_usage_percentage()

