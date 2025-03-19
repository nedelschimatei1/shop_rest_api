# Django E-commerce Platform

A comprehensive e-commerce solution built with Django, featuring robust architecture, advanced features, and optimized performance.

## 🚀 Features

### 🛒 E-commerce Core (Market App)
- **Product Management**: Categories, collections, reviews, ratings, and promotions
- **Cart System**: UUID-based identification with anonymous support
- **Order Processing**: Status tracking and item management
- **Customer Profiles**: Tiered membership system with order history

### 🔐 Authentication & User Management
- Custom user model with JWT authentication
- Role-based access control
- Permission-based API security

### 💾 Data & Media
- Secure file handling with validation
- Custom storage configuration
- Image upload with size restrictions

### 🔧 API Features
- Class-Based Views (CBVs) with ModelViewSets
- Filtering, sorting, and pagination
- Nested serialization
- CORS configuration and rate limiting

### ⚡ Performance
- Redis caching system
- Celery task queue for background processing
- Load testing with Locust
- Performance profiling with Silk

### 📊 Admin Interface
- Enhanced product management
- Order processing dashboard
- Inventory tracking
- Custom filters and actions

### 📧 Communication
- Asynchronous email notification system
- Customer alerts and order updates
- Scheduled notifications via Celery Beat

### 🔍 Testing
- Comprehensive unit and integration tests
- API endpoint testing
- Authentication flow validation
- Order process verification

## 🛠️ Technical Stack
- Django REST Framework
- Redis for caching
- Celery for task processing
- JWT for authentication
- Locust for load testing
- Silk for performance profiling
