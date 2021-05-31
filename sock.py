import socket
import _io
class socket(socket.socket):
    def __init__(self,bufsize=1024,*args,**kwargs):
        if bufsize<10:
            raise ValueError("buffer too small")
        self.bufsize=bufsize
        super().__init__(*args,**kwargs)
    def receive(self):
        result=b""
        inmsg=False
        while True:
            m=self.recvfrom(self.bufsize)
            if m==b'\x00'
                inmsg=True
            elif inmsg:
                result+=m
            elif m==b'\xff':
                inmsg=False
                break
        return result
    def post(self,data,addr):
        
        data=_io.BytesIO(data)
        self.sendto(b'\x00',addr)
        while True:
            bs=data.read(self.bufsize)
            self.sendto(bs,addr)
        self.sendto(b'\xff',addr)
        return len(data.getvalue())

