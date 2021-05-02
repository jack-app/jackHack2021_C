const jsonServer = require('json-server')
const server = jsonServer.create()
const middlewares = jsonServer.defaults()
server.use(middlewares)

// template
const topic_router = jsonServer.router('topic.json')
server.use('/template/', topic_router)
const type_router = jsonServer.router('type.json')
server.use('/template/', type_router)
const question_router = jsonServer.router('question.json')
server.use('/template/', question_router)

const diary_router = jsonServer.router('diary.json')
server.use(diary_router)
const users_router = jsonServer.router('users.json')
server.use(users_router)

server.listen(3000, () => {
  console.log('JSON Server is running')
})