from flask import Flask, render_template, request, redirect
from hdfs import InsecureClient
import os

app = Flask(__name__)

class HdfsClient:
    def __init__(self, host, port, user):
        self.hdfs = InsecureClient(f'http://{host}:{port}', user=user)

    def create_file(self, hdfs_path, file_content):
        with self.hdfs.write(hdfs_path) as writer:
            writer.write(file_content)

    def delete_file(self, hdfs_path):
        self.hdfs.delete(hdfs_path)

    def upload_file(self, local_file_path, hdfs_path):
        self.hdfs.upload(hdfs_path, local_file_path)

    def download_file(self, hdfs_path, local_file_path):
        self.hdfs.download(hdfs_path, local_file_path, overwrite=True)

hdfs_client = HdfsClient("54.245.212.236", "50070", "ubuntu")

@app.route('/')
def index():
    return redirect('/hdfs')

@app.route('/hdfs')
def hdfs():
    return render_template('hdfs.html')

@app.route('/create_file', methods=['GET'])
def create_file():
    hdfs_path = request.args.get('hdfs_path')
    file_content = request.args.get('file_content')
    hdfs_client.create_file(hdfs_path, file_content)
    return render_template('success.html')

@app.route('/delete_file', methods=['GET'])
def delete_file():
    hdfs_path = request.args.get('hdfs_path')
    hdfs_client.delete_file(hdfs_path)
    return render_template('success.html')

@app.route('/upload_file', methods=['POST'])
def upload_file():
    file = request.files['file']
    local_file_path = os.path.join(app.root_path, file.filename)
    file.save(local_file_path)
    hdfs_path = request.form.get('hdfs_path')
    hdfs_client.upload_file(local_file_path, hdfs_path)
    os.remove(local_file_path)
    return render_template('success.html')

@app.route('/download_file', methods=['GET'])
def download_file():
    hdfs_path = request.args.get('hdfs_path')
    local_file_path = request.args.get('local_file_path')
    hdfs_client.download_file(hdfs_path, local_file_path)
    return render_template('success.html')

if __name__ == '__main__':
    app.run()