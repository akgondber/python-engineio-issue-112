var http = require('http').createServer()
var io = require('socket.io')(http, { path: '/ws' })

io.on('connection', socket => {
  console.log('connected')

  socket.on('foo', data => {
    console.log('Foo: ', data)
  })
})

const port = 4001

http.listen(port, function () {
  console.log(`listening on *:${port}`)
})
