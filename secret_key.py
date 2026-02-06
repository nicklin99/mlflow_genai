import secrets

def generate_csrf_secret_key(length: int = 16) -> str:
    """
    生成安全的 CSRF Secret Key
    :param length: 密钥长度（推荐32/64，单位：字节）
    :return: 随机的十六进制格式密钥
    """
    # 生成加密安全的随机字节，转换为十六进制字符串（更易存储和使用）
    secret_key = secrets.token_hex(length)
    return secret_key

# 生成并打印 32 字节的 CSRF Secret Key
if __name__ == "__main__":
    csrf_secret = generate_csrf_secret_key()
    print(f"生成的 CSRF Secret Key: {csrf_secret}")
    print(f"密钥长度: {len(csrf_secret)} 个字符（{len(csrf_secret)//2} 字节）")