# Login Authentication Flask using JWT (Json Web Token)

## Json Web Token

### Định nghĩa

* JWT bao gồm 3 phần: Header, Payload and Signature được phân cách bởi dấu chấm "."
(header.payload.signature)

### Header

Header có 2 phần chính, loại của token và thuật toán giải mã được sử dụng

**Ví dụ:**

```json
{
    "alg": "HS256",
    "typ": "JWT"
}
```

Thông tin sẽ được encode bằng **Base64url** tạo ra 1 header hoàn chỉnh:

```
eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9
```

### Payload

Nơi chứa thông tin cần thiết để định danh user và thời hạn được access

**Ví dụ:**

```json
{
    "user_id": "1",
    "role": "admin",
    "exp": 1000,
    "iat": 800,
    "login_token": "adsadlasd"
}
```

Những giá trị như **iat, exp, iss**... được gọi là claims và có 3 loại chính:

__Register claims__: Là set các giá trị được định nghĩa từ trước bởi Jwt

* **exp**: expiration_time

* **iat**: thời gian user request đăng nhập

**Public claims**: được xác định bởi cộng đồng JWT

**Pricate claims**: được tạo riêng cho một tổ chức hay dự án cụ thể

### Signature

Giúp chúng ta bảo mật token từ client gửi về server là hợp lệ, được tạo từ 3 phần:

**Ví dụ:**

```
HMACSHA256(
  base64UrlEncode(header) + "." +
  base64UrlEncode(payload),
  secret
)
```

**HMAC SHA256** là thuật toán, 2 phần encode của header và payload + 1 secret key được tạo ra từ dự án

### Kết hợp tất cả

```
Header.Payload.Signature
```

```
eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1c2VyX2lkIjoiMSIsInJvbGUiOiJhZG1pbiIsImV4cCI6MTAwMCwiaWF0Ijo4MDAsImxvZ2luX3Rva2VuIjoiYWRzYWRsYXNkIn0.aIp-Pciwrh23ATqU1CpH8PIZ6_sa7IRZ5hhxUw-iQIM
```

### Reference: [Tìm hiểu về Json Web Token - Jwt (VIBLO)](https://viblo.asia/p/tim-hieu-ve-json-web-token-jwt-jvEla9ddlkw)

