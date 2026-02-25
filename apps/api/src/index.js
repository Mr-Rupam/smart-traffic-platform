/**
 * Smart Traffic Platform — Backend API
 * Express server entry point.
 */

require("dotenv").config();
const express = require("express");
const cors = require("cors");

const app = express();
const PORT = process.env.PORT || 4000;

// --------------- Middleware ---------------
app.use(cors());
app.use(express.json());

// --------------- Routes ---------------
app.get("/health", (_req, res) => {
  res.json({ status: "healthy", service: "api" });
});

// Mount route modules here
// app.use("/api/v1/traffic", require("./routes/traffic"));

// --------------- Start ---------------
app.listen(PORT, () => {
  console.log(`🚀 API server running on http://localhost:${PORT}`);
});

module.exports = app;
