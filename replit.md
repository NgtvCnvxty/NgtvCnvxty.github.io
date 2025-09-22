# SD Capital Systems Inc. Website

## Overview
This is a static HTML website for SD Capital Systems Inc., a Canadian financial technology company building a marketplace for Canadian dollar fixed income securities. The website provides information about their services and the types of securities they offer.

## Project Architecture
- **Type**: Static HTML website
- **Frontend**: HTML, CSS
- **Server**: Python HTTP server
- **Port**: 5000 (configured for Replit environment)

## Recent Changes (September 22, 2025)
- Imported project from GitHub
- Set up Python 3.11 environment for HTTP server
- Configured workflow to serve static files on port 5000 with 0.0.0.0 binding
- Configured deployment for autoscale target
- Verified website functionality in Replit environment

## Project Structure
- `index.html`: Main webpage with company information
- `styles.css`: Styling for the website
- `README.md`: Original project documentation

## Deployment Configuration
- Target: Autoscale (suitable for static websites)
- Command: `python -m http.server 5000 --bind 0.0.0.0`
- No build step required (static files)

## User Preferences
- Follow existing simple structure
- Maintain original styling and content