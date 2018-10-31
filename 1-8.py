from sanic import Sanic
from sanic.response import json
import excelintoSQL

app = Sanic()

@app.route('/sql/api/v1')
async def test(request):
    # return json({'hello': 'world'})

    data = excelintoSQL.from_store('double')
    return json(data)
@app.route('/sql/api/v2')
async def test(request):
    # return json({'hello': 'world'})

    data = excelintoSQL.from_store('double')
    return json(data)

if __name__ == '__main__':
    app.run(host='127.0.0.1', port=8000)