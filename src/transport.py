class Transport(object):
    """
    The actual network transport of data for a CasperFpga object.
    """
    def __init__(self, host):
        """
        
        :param host: 
        """
        self.host = host
        self.memory_devices = {}
        self.gbes = []
        self.prog_info = {'last_uploaded': '', 'last_programmed': '',
                          'system_name': ''}

    def connect(self, timeout=None):
        """
        
        :param timeout: 
        :return: 
        """
        raise NotImplementedError

    def is_running(self):
        """
        Is the FPGA programmed and running?
        :return: True or False
        """
        raise NotImplementedError

    def ping(self):
        """
        Use the 'watchdog' request to ping the FPGA host.
        :return: True or False
        """
        raise NotImplementedError

    def disconnect(self):
        """
        
        :return: 
        """
        raise NotImplementedError

    def read(self, device_name, size, offset=0):
        """
        
        :param device_name: 
        :param size: 
        :param offset: 
        :return: 
        """
        raise NotImplementedError

    def blindwrite(self, device_name, data, offset=0):
        """
        
        :param device_name: 
        :param data: 
        :param offset: 
        :return: 
        """
        raise NotImplementedError

    def listdev(self):
        """
        Get a list of the memory bus items in this design.
        :return: a list of memory devices
        """
        raise NotImplementedError

    def deprogram(self):
        """
        Deprogram the FPGA connected by this transport
        :return: 
        """
        raise NotImplementedError

    def set_igmp_version(self, version):
        """
        :param version
        :return: 
        """
        raise NotImplementedError

    def upload_to_ram_and_program(self, filename, port=-1, timeout=10,
                                  wait_complete=True):
        """
        Upload an FPG file to RAM and then program the FPGA.
        :param filename: the file to upload
        :param port: the port to use on the rx end, -1 means a random port
        :param timeout: how long to wait, seconds
        :param wait_complete: wait for the transaction to complete, return
        after upload if False
        :return:
        """
        raise NotImplementedError

    def upload_to_flash(self, binary_file, port=-1, force_upload=False,
                        timeout=30, wait_complete=True):
        """
        Upload the provided binary file to the flash filesystem.
        :param binary_file: filename of the binary file to upload
        :param port: host-side port, -1 means a random port will be used
        :param force_upload: upload the binary even if it already exists
        on the host
        :param timeout: upload timeout, in seconds
        :param wait_complete: wait for the upload to complete, or just
        kick it off
        :return:
        """
        raise NotImplementedError

    def get_system_information(self, filename=None, fpg_info=None):
        """
        
        :param filename: 
        :param fpg_info: 
        :return: processed_filename, processed_fpg_info
        """
        raise NotImplementedError

    def post_get_system_information(self):
        """
        Cleanup run after get_system_information
        :return: 
        """
        raise NotImplementedError


# end