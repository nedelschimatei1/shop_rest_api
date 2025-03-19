# 🏗️ Project Architecture Overview

## 1. Market App (Main E-commerce Logic)

### Models and Database Structure
- **Product System**
  - Products with detailed attributes (title, price, inventory, etc.)
  - Product images with file size validation
  - Collections and categories management
  - Product reviews and ratings
  - Promotions and discounts

- **Cart System**
  - UUID-based cart identification
  - Cart items with quantity validation
  - Cart persistence
  - Anonymous cart support

- **Order System**
  - Order processing and status tracking
  - Order items management
  - Payment status tracking (Pending, Complete, Failed)

- **Customer Management**
  - Customer profiles
  - Membership levels (Bronze, Silver, Gold)
  - Address management
  - Order history

### API Endpoints & Views
- All views implemented using Class-Based Views (CBVs)
- ModelViewSets for CRUD operations
- Custom permission classes
- Filtering, sorting, and pagination
- Nested serialization

### Permissions System
- Custom permission classes
  - `IsAdminOrReadOnly`
  - `ViewCustomerHistoryPermission`
  - Role-based access control

## 2. Core App (Authentication & User Management)

### User Management
- Custom user creation/serialization
- JWT authentication with refresh tokens
- User profile management
- Custom user serializers

### Signals
- Order creation signals
- Customer profile signals
- Email notification signals

## 3. Media Management

### File Handling
- Custom file storage configuration
- Image upload and validation
- File size restrictions
- Secure file serving

### Media Settings
- Configured media roots and URLs
- File type restrictions
- Storage backend configuration

## 4. Performance Testing & Monitoring

### Locust Load Testing
- Simulated user behavior
- Product browsing scenarios
- Cart operations testing
- Authentication flow testing
- Performance metrics collection

### Silk Profiling (Configured but Commented)
- Request profiling
- Database query analysis
- Performance bottleneck identification
- Response time monitoring

## 5. Caching & Performance

### Redis Cache

### Celery Task Queue
- Asynchronous task processing
- Scheduled tasks with Celery Beat
- Email notifications
- Order processing

## 6. API Features

### Authentication & Security
- JWT token authentication
- Token refresh mechanism
- CORS configuration
- API rate limiting

### Data Filtering & Search
- Django Filter backend
- Search functionality
- Dynamic filtering
- Custom filter classes

### Pagination
- Limit-offset pagination
- Configurable page size
- Custom pagination classes

## 7. Testing Infrastructure

### Unit Tests
- Model testing
- View testing
- Serializer testing
- Permission testing

### Integration Tests
- API endpoint testing
- Authentication flow testing
- Order process testing
- Cart functionality testing

## 8. Admin Interface

### Custom Admin Views
- Enhanced product management
- Order processing interface
- Customer management
- Inventory tracking
- Custom filters and actions

## 9. Background Tasks

### Celery Tasks
- Email notifications
- Order processing
- Scheduled tasks
- Customer notifications

## 10. Security Features

### Data Protection
- Password validation
- File upload validation
- CSRF protection
- Secure media handling

### API Security
- JWT token security
- Permission-based access
- Rate limiting
- CORS configuration

## 11. Development Tools

### Debug Toolbar
- SQL query debugging
- Request/response inspection
- Cache debugging
- Signal tracking

### Performance Monitoring
- Locust for load testing
- Silk for profiling (configured)
- Redis monitoring
- Database query optimization

## 12. Email System

### Email Configuration
- SMTP setup
- Email templates
- Async email sending
- Custom email backend
