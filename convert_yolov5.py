from rknn.api import RKNN

r0 = RKNN(verbose=False)
r0.config(
    target_platform='rk3566',        # ← 指定 Orange Pi 3B 芯片
    quantized_dtype='w8a8', # INT8 量化
)
r0.load_onnx(model='best.onnx')
r0.build(do_quantization=True, dataset='./dataset.txt')
r0.export_rknn('best.rknn')
r0.release()