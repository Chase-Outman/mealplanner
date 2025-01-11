import pickle

def save_object(obj, filename):
    with open(filename, 'wb') as outp:        
        pickle.dump(obj, outp, pickle.HIGHEST_PROTOCOL)

def load_objects(filename):
    with open(filename, 'rb') as inp:
        objs = pickle.load(inp)
        return objs
    
