# SD Capital Systems Inc. - Corporate Website

## Overview

This is a static corporate website for SD Capital Systems Inc., a Canadian financial technology company that specializes in fixed income securities. The website serves as an informational platform showcasing the company's marketplace for Canadian bonds, convertible bonds, and preferred shares targeted at retail investors. The site includes sections for company overview, business plan, marketplace details, and financial publications.

## User Preferences

Preferred communication style: Simple, everyday language.

## System Architecture

### Frontend Architecture
The website uses a traditional multi-page HTML structure with a consistent layout pattern across all pages. Each page follows a standard template with:
- Fixed sidebar navigation for consistent user experience
- Main content area for page-specific information
- Shared CSS styling for uniform presentation
- Simple JavaScript redirect on the homepage to automatically route users to the company overview

### Design Pattern
The architecture employs a template-based approach where each HTML page shares the same structural components:
- Navigation sidebar with company branding and menu items
- Main content area that adapts to different page content
- Footer with copyright information
- Responsive design considerations with viewport meta tags

### Content Organization
The site is organized into four main sections:
- Company Overview: High-level business description
- Company Plan: Future development plans (currently placeholder)
- Fixed Income Marketplace: Detailed list of securities offered
- Publications and Perspectives: Financial analysis documents and PDFs

### Static Asset Management
The website uses a simple file-based approach for assets:
- Single CSS file for all styling
- PDF documents stored in a dedicated directory
- Direct file linking for external document access

### Navigation Strategy
The navigation uses active state management through CSS classes to highlight the current page, providing clear visual feedback to users about their location within the site.

## External Dependencies

### Hosting Platform
- **GitHub Pages**: Used for static website hosting with the domain ngtvcnvxty.github.io
- **GitHub Repository**: Source code management and version control

### Browser Dependencies
- Standard HTML5 and CSS3 support
- JavaScript enabled for homepage redirect functionality
- PDF viewer capability for accessing financial documents

### Third-party Services
Currently, the website does not integrate with any external APIs or third-party services, maintaining a simple static architecture that ensures fast loading times and minimal dependencies.