from pywebhdfs.webhdfs import PyWebHdfsClient

hdfs = PyWebHdfsClient(host='35.89.209.197', port='50070', user_name='ubuntu')

def hdfs_delete_file(hdfs_path):
    # Delete a file from HDFS
    hdfs.delete_file_dir(hdfs_path)
    return jsonify({'message': 'File deleted successfully.'})


if __name__ == '__main__':
    hdfs_delete_file('/user/ubuntu/trial.txt')
