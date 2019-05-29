from hashlib import sha256
import time

def generate_ref(user_id):

	node_id = '47863'
	time_stamp = time.time()

	stamp = str(time_stamp).split('.')
	stamp_md5 = sha256(stamp[1].encode('utf-8')).hexdigest()
	id_md5 = sha256(str(user_id).encode('utf-8')).hexdigest()

	ref = node_id + '' + stamp_md5[:5] + '' + id_md5[:5]

	return time_stamp, ref




if __name__ == '__main__':
	print(generate_ref(1))
