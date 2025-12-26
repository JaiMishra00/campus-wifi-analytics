# WiFi Analytics Backend

## Overview
This project is a backend system designed to **collect, store, and analyze WiFi signal data** from multiple ESP32 (or similar) nodes distributed across a physical area (e.g. campus, building, or lab).

The goal is to transform raw WiFi scan data (RSSI, SSID, BSSID, channel, timestamp) into **useful spatial and temporal insights**, such as signal strength distribution, connectivity quality, and coverage patterns.

This backend is part of a larger **WiFi Analytics / Heatmap system**, where hardware nodes continuously scan nearby access points and push data to a central server for processing and visualization.

---

## Problem Statement
WiFi performance in large physical spaces is often poorly understood and manually diagnosed.  
Existing tools are:
- device-specific
- not scalable
- not designed for continuous monitoring

This project aims to build a **scalable, node-based WiFi data collection pipeline** that enables deeper analysis beyond what a single phone or laptop scan can provide.

---

## System Architecture (High-Level)

1. **WiFi Nodes (ESP32)**  
   - Perform periodic WiFi scans  
   - Capture RSSI, SSID, BSSID, channel, and timestamp  
   - Send data to backend via HTTP

2. **Backend API (FastAPI)**  
   - Receives scan data through REST endpoints  
   - Validates and structures incoming data  
   - Stores data for further analysis

3. **Analytics & Visualization (Planned)**  
   - Signal strength heatmaps  
   - Temporal analysis of network quality  
   - Zone-based WiFi performance metrics

---

## Current Features
- FastAPI-based backend server
- Structured data ingestion endpoints
- Pydantic models for WiFi scan validation
- Clean, modular project structure

---

## Tech Stack
- **Python**
- **FastAPI**
- **Pydantic**
- **Uvicorn**
- (Database & analytics layer planned)

---

## Project Status
🚧 **Work in progress**

Current focus:
- Backend API stability
- Data schema refinement
- Preparing for database integration

---

## Future Improvements
- Database integration (time-series / relational)
- RSSI normalization and filtering
- Heatmap generation
- Dashboard for visualization
- Edge-side preprocessing on nodes

---

## How to Run (Development)

```bash
# install dependencies
pip install -r requirements.txt

# run server
uvicorn app.main:app --reload
