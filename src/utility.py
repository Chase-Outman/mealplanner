import pickle

def save_object(obj, filename):
    with open(filename, 'ab') as outp:        
        pickle.dump(obj, outp, pickle.HIGHEST_PROTOCOL)

def load_objects(filename):
    objs = []
       
    with open(filename, 'rb') as inp:
        while 1:
            try:
                objs.append(pickle.load(inp))
            except EOFError:
                break
        
    return objs
    
