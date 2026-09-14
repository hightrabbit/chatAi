
"""将内容转换成hash来命名表名（collection）"""
import hashlib


class HashCalculate:
    """根据文件内容计算文件 hash"""
    #根据二进制文件，load加载的内容
    def compute_hash(self,pdf_bytes: bytes ) -> str:
        """从字节数据计算 MD5 哈希值"""
        return hashlib.md5(pdf_bytes).hexdigest()

    """从文件路径计算 MD5 哈希值（流式读取）"""
    def compute_hash_from_file(self,pdf_path: str) -> str:
        hash_md5 = hashlib.md5()
        with open(pdf_path, "rb") as f:
            for chunk in iter(lambda: f.read(4096), b""):
                hash_md5.update(chunk)
        return hash_md5.hexdigest()