"""
plantuml_diagrams.py
PlantUML diagram templates for Web application architecture.

Provides reusable PlantUML (.puml) diagram templates for:
- Use Case Diagrams
- Class Diagrams
- Sequence Diagrams
- Component Diagrams
- State Machine Diagrams
- Deployment Diagrams
- Entity Relationship Diagrams
"""

from datetime import date

TODAY = date.today().isoformat()


# ============================================================================
# USE CASE DIAGRAMS
# ============================================================================

def puml_usecase_web_app():
    """Use Case Diagram for a typical Web application."""
    return f"""@startuml web_usecase_diagram
!theme plain
title Web Application - Use Case Diagram
skinparam linetype ortho

actor Visitor as visitor
actor "Authenticated User" as user
actor Admin as admin

rectangle "Web Application" {{
  usecase "Browse Catalog" as uc_browse
  usecase "Sign In" as uc_signin
  usecase "Sign Up" as uc_signup
  usecase "View Profile" as uc_profile
  usecase "Update Profile" as uc_update_profile
  usecase "Search Products" as uc_search
  usecase "Add to Cart" as uc_add_cart
  usecase "Checkout" as uc_checkout
  usecase "View Orders" as uc_orders
  usecase "Manage Products" as uc_manage_products
  usecase "View Analytics" as uc_analytics
  usecase "Manage Users" as uc_manage_users
}}

visitor --> uc_browse
visitor --> uc_signin
visitor --> uc_signup
visitor --> uc_search

user --> uc_browse
user --> uc_profile
user --> uc_update_profile
user --> uc_search
user --> uc_add_cart
user --> uc_checkout
user --> uc_orders

admin --> uc_manage_products
admin --> uc_analytics
admin --> uc_manage_users
admin --> uc_browse

uc_signin .> uc_profile : includes
uc_checkout .> uc_orders : creates
uc_update_profile .> uc_profile : extends

@enduml
"""


def puml_usecase_auth_flow():
    """Use Case Diagram for authentication flow."""
    return f"""@startuml auth_usecase_diagram
!theme plain
title Authentication - Use Case Diagram
skinparam linetype ortho

actor User
actor "External Auth Provider" as oauth

rectangle "Auth System" {{
  usecase "Enter Credentials" as uc_enter
  usecase "Validate Credentials" as uc_validate
  usecase "Create Session" as uc_session
  usecase "Return JWT Token" as uc_token
  usecase "Sign In with OAuth" as uc_oauth
  usecase "Refresh Token" as uc_refresh
  usecase "Sign Out" as uc_signout
}}

User --> uc_enter
User --> uc_oauth
User --> uc_refresh
User --> uc_signout

uc_enter --> uc_validate
uc_validate --> uc_session
uc_session --> uc_token

uc_oauth --> oauth
oauth --> uc_token

uc_signout .> uc_token : invalidates

@enduml
"""


# ============================================================================
# CLASS DIAGRAMS
# ============================================================================

def puml_class_domain_model():
    """Class Diagram for domain model."""
    return f"""@startuml domain_model
!theme plain
title Domain Model - Class Diagram
skinparam classBackgroundColor #F0F0F0
skinparam classBorderColor #333

class User {{
  -id: UUID
  -email: string
  -name: string
  -password_hash: string
  -role: UserRole
  -created_at: DateTime
  -updated_at: DateTime
  --
  +getId(): UUID
  +getEmail(): string
  +getName(): string
  +setName(name: string): void
  +isAdmin(): boolean
  +toDTO(): UserDTO
}}

class Product {{
  -id: UUID
  -name: string
  -description: string
  -price: Decimal
  -inventory: integer
  -created_at: DateTime
  --
  +getId(): UUID
  +getName(): string
  +getPrice(): Decimal
  +isAvailable(): boolean
  +decrementInventory(qty: integer): void
  +toDTO(): ProductDTO
}}

class Order {{
  -id: UUID
  -user_id: UUID
  -status: OrderStatus
  -total_amount: Decimal
  -items: OrderItem[]
  -created_at: DateTime
  -updated_at: DateTime
  --
  +getId(): UUID
  +getStatus(): OrderStatus
  +getTotalAmount(): Decimal
  +getItems(): OrderItem[]
  +canCancel(): boolean
  +cancel(): void
}}

class OrderItem {{
  -id: UUID
  -order_id: UUID
  -product_id: UUID
  -quantity: integer
  -unit_price: Decimal
  --
  +getQuantity(): integer
  +getUnitPrice(): Decimal
  +getSubtotal(): Decimal
}}

class Cart {{
  -id: UUID
  -user_id: UUID
  -items: CartItem[]
  -created_at: DateTime
  --
  +addItem(product: Product, qty: integer): void
  +removeItem(product_id: UUID): void
  +getItems(): CartItem[]
  +getTotal(): Decimal
  +isEmpty(): boolean
  +checkout(): Order
}}

class CartItem {{
  -id: UUID
  -cart_id: UUID
  -product_id: UUID
  -quantity: integer
  --
  +getQuantity(): integer
  +updateQuantity(qty: integer): void
}}

enum UserRole {{
  ADMIN
  USER
  GUEST
}}

enum OrderStatus {{
  PENDING
  CONFIRMED
  SHIPPED
  DELIVERED
  CANCELLED
}}

User --> UserRole
Order --> OrderStatus
Order "1" *-- "*" OrderItem
Cart "1" *-- "*" CartItem
OrderItem --> Product
CartItem --> Product
Cart --> User
Order --> User

@enduml
"""


def puml_class_services():
    """Class Diagram for application services."""
    return f"""@startuml services_diagram
!theme plain
title Application Services - Class Diagram
skinparam classBackgroundColor #E8F4F8

interface IAuthService {{
  +signIn(email: string, password: string): AuthSession
  +signOut(): void
  +getCurrentUser(): User
  +refreshToken(token: string): AuthSession
}}

interface IProductService {{
  +getProduct(id: UUID): Product
  +listProducts(filters: Filter): Product[]
  +searchProducts(query: string): Product[]
  +updateProduct(id: UUID, data: UpdateProductDTO): Product
  +deleteProduct(id: UUID): void
}}

interface IOrderService {{
  +createOrder(user_id: UUID, items: CartItem[]): Order
  +getOrder(id: UUID): Order
  +getUserOrders(user_id: UUID): Order[]
  +cancelOrder(id: UUID): void
}}

class AuthService {{
  -userRepository: UserRepository
  -tokenService: TokenService
  -passwordHasher: PasswordHasher
  --
  +signIn(email: string, password: string): AuthSession
  +signOut(): void
  +getCurrentUser(): User
  +refreshToken(token: string): AuthSession
}}

class ProductService {{
  -productRepository: ProductRepository
  -cacheService: CacheService
  --
  +getProduct(id: UUID): Product
  +listProducts(filters: Filter): Product[]
  +searchProducts(query: string): Product[]
  +updateProduct(id: UUID, data: UpdateProductDTO): Product
  +deleteProduct(id: UUID): void
}}

class OrderService {{
  -orderRepository: OrderRepository
  -cartService: CartService
  -notificationService: NotificationService
  --
  +createOrder(user_id: UUID, items: CartItem[]): Order
  +getOrder(id: UUID): Order
  +getUserOrders(user_id: UUID): Order[]
  +cancelOrder(id: UUID): void
}}

AuthService ..|> IAuthService
ProductService ..|> IProductService
OrderService ..|> IOrderService

@enduml
"""


# ============================================================================
# SEQUENCE DIAGRAMS
# ============================================================================

def puml_sequence_login_flow():
    """Sequence Diagram for login flow."""
    return f"""@startuml login_sequence
!theme plain
title Login Flow - Sequence Diagram
participant User
participant LoginPage as "Login Page"
participant useLoginForm as "useLoginForm Hook"
participant AuthService
participant "API Client"
participant "Auth API"

User -> LoginPage: Submit email & password
activate LoginPage

LoginPage -> useLoginForm: handleSubmit(credentials)
activate useLoginForm

useLoginForm -> AuthService: signIn(email, password)
activate AuthService

AuthService -> "API Client": POST /auth/login
activate "API Client"

"API Client" -> "Auth API": HTTP POST
activate "Auth API"

"Auth API" --> "API Client": {{accessToken, user, refreshToken}}
deactivate "Auth API"

"API Client" --> AuthService: {{accessToken, user, refreshToken}}
deactivate "API Client"

AuthService -> AuthService: storeSession(accessToken)
AuthService --> useLoginForm: AuthSession
deactivate AuthService

useLoginForm -> useLoginForm: setAuthState(session)
useLoginForm --> LoginPage: success state
deactivate useLoginForm

LoginPage -> LoginPage: navigate('/dashboard')
LoginPage --> User: Redirect to dashboard
deactivate LoginPage

@enduml
"""


def puml_sequence_checkout_flow():
    """Sequence Diagram for checkout flow."""
    return f"""@startuml checkout_sequence
!theme plain
title Checkout Flow - Sequence Diagram
participant User
participant CheckoutPage
participant "Order Service"
participant "Payment Service"
participant "Payment Gateway"
participant Database

User -> CheckoutPage: Click checkout
activate CheckoutPage

CheckoutPage -> CheckoutPage: Validate cart
CheckoutPage -> CheckoutPage: Get shipping address

User -> CheckoutPage: Enter payment details
CheckoutPage -> "Payment Service": processPayment(amount, details)
activate "Payment Service"

"Payment Service" -> "Payment Gateway": charge(amount, token)
activate "Payment Gateway"

alt Payment Successful
  "Payment Gateway" --> "Payment Service": success
  "Payment Service" -> "Order Service": createOrder(cart, shipping, payment)
  activate "Order Service"

  "Order Service" -> Database: save(order)
  Database --> "Order Service": order_id

  "Order Service" --> "Payment Service": Order
  deactivate "Order Service"

  "Payment Service" --> CheckoutPage: {{success, orderId}}
  deactivate "Payment Gateway"

  CheckoutPage -> CheckoutPage: Show success page
  CheckoutPage --> User: Order confirmed

else Payment Failed
  "Payment Gateway" --> "Payment Service": failure
  deactivate "Payment Gateway"

  "Payment Service" --> CheckoutPage: {{error, message}}
  CheckoutPage -> CheckoutPage: Show error
  CheckoutPage --> User: Payment failed
end

deactivate "Payment Service"
deactivate CheckoutPage

@enduml
"""


# ============================================================================
# COMPONENT DIAGRAMS
# ============================================================================

def puml_component_frontend_architecture():
    """Component Diagram for frontend architecture."""
    return f"""@startuml frontend_components
!theme plain
title Frontend Architecture - Component Diagram
skinparam componentStyle rectangle

package "React Application" {{
  component App
  component Router
  component AppLayout

  package "Pages" {{
    component HomePage
    component ProductPage
    component CheckoutPage
    component OrderPage
  }}

  package "Features" {{
    component LoginFeature
    component CartFeature
    component ProfileFeature
  }}

  package "Shared Components" {{
    component Button
    component Modal
    component Form
    component Header
    component Footer
  }}

  package "Hooks" {{
    component useAuth
    component useCart
    component useFetch
  }}

  package "Services" {{
    component AuthService
    component ProductService
    component OrderService
  }}

  package "API Client" {{
    component HttpClient
    component TokenManager
  }}
}}

package "External Services" {{
  component "Backend API"
  component "Payment Gateway"
  component "Analytics"
}}

App --> Router
Router --> AppLayout
AppLayout --> HomePage
AppLayout --> ProductPage
AppLayout --> CheckoutPage
AppLayout --> OrderPage

HomePage --> LoginFeature
HomePage --> CartFeature
CheckoutPage --> CartFeature
OrderPage --> ProfileFeature

LoginFeature --> useAuth
CartFeature --> useCart
ProductPage --> useFetch

useAuth --> AuthService
useCart --> ProductService
useFetch --> OrderService

AuthService --> HttpClient
ProductService --> HttpClient
OrderService --> HttpClient

HttpClient --> TokenManager
TokenManager --> "Backend API"

CheckoutPage --> "Payment Gateway"
App --> Analytics

@enduml
"""


def puml_component_system_architecture():
    """Component Diagram for system architecture."""
    return f"""@startuml system_components
!theme plain
title System Architecture - Component Diagram

package "Client Layer" {{
  component "React App"
  component "TypeScript"
  component "Vite"
}}

package "API Layer" {{
  component "REST API"
  component "Authentication"
  component "Validation"
}}

package "Application Layer" {{
  component "Auth Service"
  component "Product Service"
  component "Order Service"
  component "User Service"
}}

package "Data Layer" {{
  component "PostgreSQL"
  component "Redis Cache"
  component "File Storage"
}}

package "External Services" {{
  component "Payment Gateway"
  component "Email Service"
  component "Analytics"
}}

"React App" --> "REST API"
"TypeScript" --> "React App"
"Vite" --> "React App"

"REST API" --> Authentication
"REST API" --> Validation
"REST API" --> "Auth Service"
"REST API" --> "Product Service"
"REST API" --> "Order Service"
"REST API" --> "User Service"

"Auth Service" --> "PostgreSQL"
"Product Service" --> "PostgreSQL"
"Product Service" --> "Redis Cache"
"Order Service" --> "PostgreSQL"
"User Service" --> "PostgreSQL"

"Order Service" --> "Payment Gateway"
"Auth Service" --> "Email Service"
"React App" --> Analytics

@enduml
"""


# ============================================================================
# STATE MACHINE DIAGRAMS
# ============================================================================

def puml_state_form_validation():
    """State Machine Diagram for form validation."""
    return f"""@startuml form_states
!theme plain
title Form Validation - State Machine Diagram
skinparam state {{
  BackgroundColor #F0F0F0
  BorderColor #333
}}

[*] --> Idle

Idle --> Validating: user submits\n(validate)

Validating --> Validated: all fields valid
Validating --> Invalid: validation errors

Invalid --> Idle: user edits field

Validated --> Submitting: submit to API

Submitting --> Success: success response
Submitting --> Error: error response

Error --> Idle: user retries

Success --> [*]: order confirmed

@enduml
"""


def puml_state_order_lifecycle():
    """State Machine Diagram for order lifecycle."""
    return f"""@startuml order_states
!theme plain
title Order Lifecycle - State Machine Diagram
skinparam state {{
  BackgroundColor #F0F0F0
  BorderColor #333
}}

[*] --> Pending: order created

Pending --> Confirmed: payment authorized
Pending --> Cancelled: user cancels\nor payment fails

Confirmed --> Processing: order processing

Processing --> Shipped: items packed\nand shipped

Shipped --> Delivered: delivery confirmed

Delivered --> [*]: order complete

Cancelled --> [*]: order cancelled

Pending --> Cancelled: timeout (24h)
Confirmed --> Pending: retry\nif payment fails

@enduml
"""


def puml_state_auth_session():
    """State Machine Diagram for authentication session."""
    return f"""@startuml auth_states
!theme plain
title Authentication Session - State Machine Diagram
skinparam state {{
  BackgroundColor #F0F0F0
  BorderColor #333
}}

[*] --> Unauthenticated

Unauthenticated --> Authenticating: user enters\ncredentials

Authenticating --> Authenticated: credentials valid
Authenticating --> Unauthenticated: credentials invalid

Authenticated --> TokenRefreshing: token expiring soon

TokenRefreshing --> Authenticated: new token obtained
TokenRefreshing --> Unauthenticated: refresh failed

Authenticated --> Unauthenticated: user logs out
Authenticated --> Unauthenticated: token expired

Unauthenticated --> [*]: session ended

@enduml
"""


# ============================================================================
# DEPLOYMENT DIAGRAMS
# ============================================================================

def puml_deployment_architecture():
    """Deployment Diagram for application infrastructure."""
    return f"""@startuml deployment_diagram
!theme plain
title Deployment Architecture - Deployment Diagram
skinparam artifact {{
  BackgroundColor #E8F4F8
  BorderColor #333
}}

node "Client Layer" {{
  artifact browser [
    Browser
    ----
    React App
  ]
}}

node "CDN / Static Hosting" {{
  artifact cdn [
    CDN (Vercel/Netlify)
    ----
    Static Assets
    JS/CSS Bundles
  ]
}}

node "API Server" {{
  artifact api_server [
    Node.js Server
    ----
    Express/Fastify
    Application Services
  ]
}}

node "Data Layer" {{
  artifact database [
    PostgreSQL
    ----
    User Data
    Products
    Orders
  ]

  artifact cache [
    Redis
    ----
    Session Cache
    Query Cache
  ]
}}

node "External Services" {{
  artifact payment [
    Payment Gateway
    ----
    Stripe/PayPal
  ]

  artifact email [
    Email Service
    ----
    SendGrid/AWS SES
  ]
}}

browser --> cdn: fetch assets
browser --> api_server: API requests
api_server --> database: read/write
api_server --> cache: get/set cache
api_server --> payment: payment processing
api_server --> email: send emails

@enduml
"""


# ============================================================================
# ENTITY RELATIONSHIP DIAGRAMS (ERD)
# ============================================================================

def puml_erd_database_schema():
    """Entity Relationship Diagram for database schema."""
    return f"""@startuml database_erd
!theme plain
title Database Schema - Entity Relationship Diagram
skinparam entity {{
  BackgroundColor #F0F0F0
  BorderColor #333
}}

entity users {{
  *id : UUID
  --
  email : string (UNIQUE, NOT NULL)
  name : string
  password_hash : string
  role : enum (ADMIN, USER)
  email_verified : boolean
  created_at : timestamp
  updated_at : timestamp
}}

entity products {{
  *id : UUID
  --
  name : string (NOT NULL)
  description : text
  price : decimal (NOT NULL)
  inventory : integer
  category : string
  created_at : timestamp
  updated_at : timestamp
}}

entity orders {{
  *id : UUID
  --
  user_id : UUID (NOT NULL, FK)
  status : enum (PENDING, CONFIRMED, SHIPPED, DELIVERED, CANCELLED)
  total_amount : decimal
  shipping_address : string
  created_at : timestamp
  updated_at : timestamp
}}

entity order_items {{
  *id : UUID
  --
  order_id : UUID (NOT NULL, FK)
  product_id : UUID (NOT NULL, FK)
  quantity : integer (NOT NULL)
  unit_price : decimal (NOT NULL)
}}

entity carts {{
  *id : UUID
  --
  user_id : UUID (UNIQUE, FK)
  created_at : timestamp
  updated_at : timestamp
}}

entity cart_items {{
  *id : UUID
  --
  cart_id : UUID (NOT NULL, FK)
  product_id : UUID (NOT NULL, FK)
  quantity : integer (NOT NULL)
}}

entity sessions {{
  *id : UUID
  --
  user_id : UUID (NOT NULL, FK)
  access_token : string
  refresh_token : string
  expires_at : timestamp
  created_at : timestamp
}}

users ||--o{{ orders : "places"
users ||--o{{ carts : "owns"
users ||--o{{ sessions : "has"
products ||--o{{ order_items : "contained in"
orders ||--o{{ order_items : "contains"
products ||--o{{ cart_items : "contained in"
carts ||--o{{ cart_items : "contains"

@enduml
"""


# ============================================================================
# EXPORT TEMPLATES
# ============================================================================

def get_all_plantuml_diagrams():
    """Returns a dictionary of all PlantUML diagram templates."""
    return {
        "usecase_web_app": {
            "name": "web_usecase_diagram.puml",
            "description": "Use Case Diagram for Web Application",
            "type": "use-case",
            "content": puml_usecase_web_app(),
        },
        "usecase_auth": {
            "name": "auth_usecase_diagram.puml",
            "description": "Use Case Diagram for Authentication",
            "type": "use-case",
            "content": puml_usecase_auth_flow(),
        },
        "class_domain": {
            "name": "domain_model.puml",
            "description": "Class Diagram for Domain Model",
            "type": "class",
            "content": puml_class_domain_model(),
        },
        "class_services": {
            "name": "services_diagram.puml",
            "description": "Class Diagram for Application Services",
            "type": "class",
            "content": puml_class_services(),
        },
        "sequence_login": {
            "name": "login_sequence.puml",
            "description": "Sequence Diagram for Login Flow",
            "type": "sequence",
            "content": puml_sequence_login_flow(),
        },
        "sequence_checkout": {
            "name": "checkout_sequence.puml",
            "description": "Sequence Diagram for Checkout Flow",
            "type": "sequence",
            "content": puml_sequence_checkout_flow(),
        },
        "component_frontend": {
            "name": "frontend_components.puml",
            "description": "Component Diagram for Frontend Architecture",
            "type": "component",
            "content": puml_component_frontend_architecture(),
        },
        "component_system": {
            "name": "system_architecture.puml",
            "description": "Component Diagram for System Architecture",
            "type": "component",
            "content": puml_component_system_architecture(),
        },
        "state_form": {
            "name": "form_states.puml",
            "description": "State Machine for Form Validation",
            "type": "state",
            "content": puml_state_form_validation(),
        },
        "state_order": {
            "name": "order_states.puml",
            "description": "State Machine for Order Lifecycle",
            "type": "state",
            "content": puml_state_order_lifecycle(),
        },
        "state_auth": {
            "name": "auth_states.puml",
            "description": "State Machine for Authentication Session",
            "type": "state",
            "content": puml_state_auth_session(),
        },
        "deployment": {
            "name": "deployment_architecture.puml",
            "description": "Deployment Diagram for Infrastructure",
            "type": "deployment",
            "content": puml_deployment_architecture(),
        },
        "erd": {
            "name": "database_erd.puml",
            "description": "Entity Relationship Diagram for Database",
            "type": "erd",
            "content": puml_erd_database_schema(),
        },
    }


if __name__ == "__main__":
    # Display all available diagrams
    diagrams = get_all_plantuml_diagrams()
    print(f"PlantUML Diagrams Available: {len(diagrams)}\n")
    for key, diagram in diagrams.items():
        print(f"[OK] {diagram['name']:40} - {diagram['description']}")
