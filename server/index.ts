import express from 'express'
// import { graphqlHTTP } from "express-graphql";
// import { buildSchema } from "graphql";

const app = express()

const PORT = process.env.PORT || 4500

app.get('/api', (req, res) => {
  res.send('Hello World!!')
})

app.listen(PORT, () => console.log(`Server started on ${PORT}`))

// const schema = buildSchema(`
//   type Query {
//     hello: String
//   }
// `);

// const root = {
//   hello: () => {
//     return 'Hello world!';
//   },
// };

// app.use('/graphql', graphqlHTTP({
//   schema: schema,
//   rootValue: root,
//   graphiql: true,
// }));
// app.listen(4500);
// console.log('Running a GraphQL API server at http://localhost:4500/graphql');
