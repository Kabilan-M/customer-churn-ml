# Real-Time ML Inference API

A production-style REST API for real-time Titanic survival prediction using a trained Scikit-Learn champion model.

## Project Overview

This project packages a trained machine-learning classification model into a FastAPI REST service.

The API accepts Titanic passenger information as JSON and returns:
- Predicted class
- Prediction label
- Probability of negative class
- Probability of positive class

## Architecture

Client
→ FastAPI REST API
→ Pydantic Validation
→ Preprocessing Pipeline
→ Champion ML Model
→ Prediction Probabilities
→ JSON Response

## API Endpoints

### GET /

Returns a message confirming that the API is running.

### GET /health

Returns API and model health status.

Example:

```json
{
  "status": "healthy",
  "model_loaded": true
}