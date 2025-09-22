# SD Capital Systems Inc. Website

## Overview

This repository contains the source code for SD Capital Systems Inc.'s corporate website, a Canadian financial technology company focused on fixed income securities. The website serves as an informational platform showcasing the company's marketplace for Canadian bonds, convertible bonds, and preferred shares targeted at retail investors. The site is hosted on GitHub Pages and provides company information, business plans, marketplace details, and financial publications.

## User Preferences

Preferred communication style: Simple, everyday language.

## System Architecture

### Frontend Architecture
The website follows a simple multi-page HTML architecture with a consistent navigation structure across all pages. The design uses a sidebar navigation pattern with a fixed layout that provides easy access to all sections. JavaScript is minimally used, with only a redirect script on the homepage to automatically navigate users to the company overview page.

### Page Structure and Navigation
The site consists of five main HTML pages organized around a central navigation system:
- Homepage (index.html) with automatic redirect to company overview
- Company Overview page providing business description
- Company Plan page (currently placeholder content)
- Fixed Income Marketplace page detailing available securities
- Publications and Perspectives page with downloadable PDF resources

### Styling and Design System
The CSS follows a clean, professional design with a consistent color scheme using green accents (#339966) for branding and gray borders for visual separation. The layout uses flexbox for the main container structure with a fixed sidebar navigation and responsive content area.

### Content Management
Static HTML content is used throughout with manual content updates. The publications section includes links to PDF documents stored in a dedicated PDFs directory, allowing for easy addition of new financial analysis documents.

## External Dependencies

### Hosting Platform
- **GitHub Pages**: Used for static site hosting and deployment
- **Domain**: Currently hosted at https://ngtvcnvxty.github.io/

### Asset Management
- **PDF Storage**: Local file storage for financial publications and analysis documents
- **No External CDNs**: All styles and scripts are self-hosted for maximum control and reliability

### Browser Compatibility
- **Standard HTML5/CSS3**: Compatible with all modern browsers
- **No JavaScript Frameworks**: Minimal JavaScript dependency reduces compatibility issues