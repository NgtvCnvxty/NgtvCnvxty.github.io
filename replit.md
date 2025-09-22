# Replit.md - SD Capital Systems Inc. Website

## Overview

This is a static corporate website for SD Capital Systems Inc., a Canadian financial technology company focused on building a marketplace for fixed income securities. The website serves as an informational platform showcasing the company's mission to increase retail investor access to bonds, convertible bonds, and preferred shares in the Canadian market. The site includes company information, business plans, marketplace details, and financial analysis publications.

## User Preferences

Preferred communication style: Simple, everyday language.

## System Architecture

### Frontend Architecture
- **Static HTML/CSS Website**: Pure vanilla HTML5 with CSS3 styling, no JavaScript frameworks or build tools required
- **Multi-page Structure**: Traditional server-side navigation with separate HTML files for each section
- **Responsive Design**: Mobile-first approach with viewport meta tags and flexible layouts
- **Component Consistency**: Shared navigation sidebar and footer across all pages with consistent styling

### Navigation and Routing
- **Client-side Redirect**: Index page automatically redirects users to company-overview.html as the default landing page
- **Sidebar Navigation**: Fixed-position navigation menu with active state indicators
- **Static Routing**: Direct file-based routing with .html extensions

### Content Management
- **Static Content**: All content is hardcoded in HTML with placeholder sections for future content ([TBD] sections)
- **PDF Integration**: External PDF documents served from a PDFs/ directory for publications and analysis
- **External Links**: PDFs open in new tabs with security attributes (target="_blank" rel="noopener")

### Styling Architecture
- **Single CSS File**: Centralized styles.css file with global styling rules
- **Color Scheme**: Professional green and gray color palette with white backgrounds
- **Typography**: Arial font family with consistent line-height of 1.4
- **Layout System**: Flexbox-based layout with fixed sidebar and flexible content area

## External Dependencies

### Hosting Platform
- **GitHub Pages**: Static site hosting with automatic deployment from repository
- **Domain**: Hosted at https://ngtvcnvxty.github.io/

### Content Dependencies
- **PDF Documents**: External PDF files for financial analysis and publications stored in PDFs/ directory
- **No External APIs**: Completely self-contained static website with no external API calls
- **No Database**: All content is static HTML with no dynamic data requirements
- **No Authentication**: Public-facing informational website with no user accounts or login systems

### Browser Requirements
- **Modern HTML5 Support**: Requires browsers supporting HTML5 semantic elements and CSS3 features
- **JavaScript Enabled**: Required for index page redirect functionality
- **No Framework Dependencies**: Pure vanilla implementation with no external JavaScript libraries or CSS frameworks