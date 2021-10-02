import dropbox
class Transferdata:
    def __init__(self,access_token):
        self.access_token=access_token

    def upload_file(self, file_from, file_to):
        dbx= dropbox.Dropbox(self.access_token)
        f=open(file_from,"rb")
        dbx.files_upload(f.read(), file_to)
def main():
    access_token="HWYGtAPdo5QAAAAAAAAAAfdVHnrueAupj2Tg5HZQYB5PJcJf3c1OX-Ye3OQx8Gqp"
    transferdata=Transferdata(access_token)
    file_from=input("Enter The File Path To Transfer")
    file_to=input("Enter The Full Path to Upload To The Dropbox")     
    transferdata.upload_file(file_from, file_to)

    print("File Has Been Moved!!")
main()       