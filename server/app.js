
import express from "express";
import cors from "cors";

const app = express();

app.use(cors());  //frontend can access the backend api
app.use(express.json());

app.get("/api/health", (req, res) => {
    res.status(200).json({
        status: "OK",
        message: "StockLens API is running"
    });
});

export default app;
