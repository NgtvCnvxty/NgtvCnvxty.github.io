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
- Transformed single-page website into professional multi-page structure
- Implemented left-side navigation with 4 sections: Company Overview, Company Plan, Fixed Income Marketplace, Publications and Perspectives
- Applied company branding: green RGB(51,153,102) titles, gray RGB(232,231,232) borders, black text
- Added PDF publishing functionality to Publications section
- Achieved pixel-perfect alignment of titles and underlines across all pages
- Organized file structure: src/ folder for HTML/CSS, PDFs/ folder for documents
- Configured workflow to serve from src/ directory on port 5000 with 0.0.0.0 binding
- Configured deployment for autoscale target

## Project Structure
```
├── src/                          # Source files
│   ├── index.html               # Landing page (redirects to Company Overview)
│   ├── company-overview.html    # Company Overview page
│   ├── company-plan.html        # Company Plan page  
│   ├── fixed-income-marketplace.html # Fixed Income Marketplace page
│   ├── founder-perspectives.html # Publications and Perspectives page
│   └── styles.css               # Main stylesheet
├── PDFs/                        # PDF documents
│   ├── USDCAD_Forward_Rate.pdf  # Forward Exchange Rate Calculation
│   └── Natural_Cubic_Spline_Python.pdf # Natural Cubic Spline - Python
├── README.md                    # Original project documentation
└── replit.md                    # Project summary and preferences
```

## Deployment Configuration
- Target: Autoscale (suitable for static websites)
- Command: `cd src && python -m http.server 5000 --bind 0.0.0.0`
- No build step required (static files)

## User Preferences
- Follow existing simple structure
- Maintain original styling and content