import bottle, json
from bottle import post, get

app = application = bottle.default_app()

@post('/names')
def creation_handler():
    '''Handles name creation'''
    
    try:
        try:
            data = request.json()
        except:
            raise ValueError
        
        if data is None:
            raise ValueError
        
        try:
            if namepattern.match(data['name']) is None:
                raise ValueError
            name = data['name']
        except (TypeError, KeyError):
            raise ValueError

        if name in _names:
            raise KeyError

    except ValueError:
        #devolvemos 400 bad request
        response.status = 400
        return

    except KeyError:
        #devolvemos conflicto 409
        response.status = 409
        return

    #add nombre
    _names.add(name)

    #return 200 success
    response.headers['Content-Type'] = 'application/json'
    return json.dumps({'name': name})    

@get('/names')
def listing_handler():
    '''Handles name listing'''
    
    response.headers['Content-Type'] = 'application/json'
    response.headers['Cache-Control'] = 'no-cache'
    return json.dumps({'names': list(_names)})

if __name__ == '__main__':
    bottle.run(host = '127.0.0.1', port = 8000)
