import datetime
import pickle
import requests

def get_protein_sequence(uniprot_id):
    url = f"https://www.uniprot.org/uniprot/{uniprot_id}.fasta"
    response = requests.get(url)
    response.raise_for_status()
    fasta = response.text.strip().split('\n', 1)[1]
    sequence = ''.join(fasta.split('\n'))
    return sequence


# Define a function that logs a message with a timestamp
def log_message(message):
    timestamp = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    print(f"[{timestamp}] {message}")

    
def save_obj(data, save_filename, save_path):
    tf = open(f"{save_path}/{save_filename}", "wb")
    pickle.dump(data, tf)
    tf.close()
    
def load_obj(save_filename, save_path):
    tf = open(f"{save_path}/{save_filename}", "rb")
    data = pickle.load(tf)
    tf.close()
    return data