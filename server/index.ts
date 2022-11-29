import express from 'express'
import { graphqlHTTP } from 'express-graphql'
import { buildSchema } from 'graphql'

// Construct a schema, using GraphQL schema language
const schema = buildSchema(`
  input MessageInput {
    name: String
    title: String
  }

  type Message {
    id: ID!
    name: String
    title: String
  }

  type Query {
    getMessage(id: ID!): Message
  }

  type Mutation {
    createMessage(input: MessageInput): Message
    updateMessage(id: ID!, input: MessageInput): Message
  }
`)

class Message {
  id: any
  content: any
  author: any
  constructor(id: any, { content, author }: any) {
    this.id = id
    this.content = content
    this.author = author
  }
}

// The root provides the top-level API endpoints
const fakeDatabase: any = {}
const root = {
  getMessage: ({ id }: any) => {
    if (!fakeDatabase[id]) {
      throw new Error('no message exists with id ' + id)
    }
    return new Message(id, fakeDatabase[id])
  },
  createMessage: ({ input }: any) => {
    // Create a random id for our "database".
    const id = require('crypto').randomBytes(10).toString('hex')

    fakeDatabase[id] = input
    return new Message(id, input)
  },
  updateMessage: ({ id, input }: any) => {
    if (!fakeDatabase[id]) {
      throw new Error('no message exists with id ' + id)
    }
    fakeDatabase[id] = input
    return new Message(id, input)
  },
}

const app = express()

app.use(
  '/graphql',
  graphqlHTTP({
    schema: schema,
    rootValue: root,
    graphiql: true,
  }),
)
app.listen(4500)
console.log('Running server at http://localhost:4500')
