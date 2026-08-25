import h5py

def print_h5_structure(name, obj):
    """递归回调：打印文件里每个节点的路径和基本信息"""
    if isinstance(obj, h5py.Dataset):
        print(f"[Dataset ] {name}  形状={obj.shape}  类型={obj.dtype}")
    else:
        print(f"[Group   ] {name}/")

def explore_h5(path):
    with h5py.File(path, "r") as f:
        print(f"文件: {path}")
        print("根节点下的一级键: ", list(f.keys()))
        print("-" * 60)

        # 递归遍历整个文件结构
        f.visititems(print_h5_structure)

        # 根级数据集预览（示例）
        for key in f.keys():
            item = f[key]
            if isinstance(item, h5py.Dataset):
                print(f"\n预览 {key}:")
                print(item[()])          # 读取全部数据
if __name__ == "__main__":
    explore_h5("k0p35_a0p10_nppc500_t40_no_w_sample200.h5") 