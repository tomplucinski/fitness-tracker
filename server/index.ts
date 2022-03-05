import express from "express";

const app = express();

const PORT = process.env.PORT || 4500;

app.get("/api", (req, res) => {
  res.send("Hello World!!");
});

app.listen(PORT, () => console.log(`Server started on ${PORT}`));
