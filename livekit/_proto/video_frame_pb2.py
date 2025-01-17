# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: video_frame.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from . import handle_pb2 as handle__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x11video_frame.proto\x12\rlivekit.proto\x1a\x0chandle.proto\"k\n\x17\x41llocVideoBufferRequest\x12\x31\n\x04type\x18\x01 \x01(\x0e\x32#.livekit.proto.VideoFrameBufferType\x12\r\n\x05width\x18\x02 \x01(\r\x12\x0e\n\x06height\x18\x03 \x01(\r\"P\n\x18\x41llocVideoBufferResponse\x12\x34\n\x06\x62uffer\x18\x01 \x01(\x0b\x32$.livekit.proto.OwnedVideoFrameBuffer\"[\n\x15NewVideoStreamRequest\x12\x14\n\x0ctrack_handle\x18\x01 \x01(\x04\x12,\n\x04type\x18\x02 \x01(\x0e\x32\x1e.livekit.proto.VideoStreamType\"I\n\x16NewVideoStreamResponse\x12/\n\x06stream\x18\x01 \x01(\x0b\x32\x1f.livekit.proto.OwnedVideoStream\"\x7f\n\x15NewVideoSourceRequest\x12,\n\x04type\x18\x01 \x01(\x0e\x32\x1e.livekit.proto.VideoSourceType\x12\x38\n\nresolution\x18\x02 \x01(\x0b\x32$.livekit.proto.VideoSourceResolution\"I\n\x16NewVideoSourceResponse\x12/\n\x06source\x18\x01 \x01(\x0b\x32\x1f.livekit.proto.OwnedVideoSource\"v\n\x18\x43\x61ptureVideoFrameRequest\x12\x15\n\rsource_handle\x18\x01 \x01(\x04\x12,\n\x05\x66rame\x18\x02 \x01(\x0b\x32\x1d.livekit.proto.VideoFrameInfo\x12\x15\n\rbuffer_handle\x18\x03 \x01(\x04\"\x1b\n\x19\x43\x61ptureVideoFrameResponse\"l\n\rToI420Request\x12\x0e\n\x06\x66lip_y\x18\x01 \x01(\x08\x12-\n\x04\x61rgb\x18\x02 \x01(\x0b\x32\x1d.livekit.proto.ArgbBufferInfoH\x00\x12\x14\n\nyuv_handle\x18\x03 \x01(\x04H\x00\x42\x06\n\x04\x66rom\"F\n\x0eToI420Response\x12\x34\n\x06\x62uffer\x18\x01 \x01(\x0b\x32$.livekit.proto.OwnedVideoFrameBuffer\"\xb6\x01\n\rToArgbRequest\x12\x15\n\rbuffer_handle\x18\x01 \x01(\x04\x12\x0f\n\x07\x64st_ptr\x18\x02 \x01(\x04\x12\x32\n\ndst_format\x18\x03 \x01(\x0e\x32\x1e.livekit.proto.VideoFormatType\x12\x12\n\ndst_stride\x18\x04 \x01(\r\x12\x11\n\tdst_width\x18\x05 \x01(\r\x12\x12\n\ndst_height\x18\x06 \x01(\r\x12\x0e\n\x06\x66lip_y\x18\x07 \x01(\x08\"\x10\n\x0eToArgbResponse\"D\n\x0fVideoResolution\x12\r\n\x05width\x18\x01 \x01(\r\x12\x0e\n\x06height\x18\x02 \x01(\r\x12\x12\n\nframe_rate\x18\x03 \x01(\x01\"|\n\x0e\x41rgbBufferInfo\x12\x0b\n\x03ptr\x18\x01 \x01(\x04\x12.\n\x06\x66ormat\x18\x02 \x01(\x0e\x32\x1e.livekit.proto.VideoFormatType\x12\x0e\n\x06stride\x18\x03 \x01(\r\x12\r\n\x05width\x18\x04 \x01(\r\x12\x0e\n\x06height\x18\x05 \x01(\r\"V\n\x0eVideoFrameInfo\x12\x14\n\x0ctimestamp_us\x18\x01 \x01(\x03\x12.\n\x08rotation\x18\x02 \x01(\x0e\x32\x1c.livekit.proto.VideoRotation\"\x97\x02\n\x14VideoFrameBufferInfo\x12\x38\n\x0b\x62uffer_type\x18\x01 \x01(\x0e\x32#.livekit.proto.VideoFrameBufferType\x12\r\n\x05width\x18\x02 \x01(\r\x12\x0e\n\x06height\x18\x03 \x01(\r\x12\x31\n\x03yuv\x18\x04 \x01(\x0b\x32\".livekit.proto.PlanarYuvBufferInfoH\x00\x12\x36\n\x06\x62i_yuv\x18\x05 \x01(\x0b\x32$.livekit.proto.BiplanarYuvBufferInfoH\x00\x12\x31\n\x06native\x18\x06 \x01(\x0b\x32\x1f.livekit.proto.NativeBufferInfoH\x00\x42\x08\n\x06\x62uffer\"y\n\x15OwnedVideoFrameBuffer\x12-\n\x06handle\x18\x01 \x01(\x0b\x32\x1d.livekit.proto.FfiOwnedHandle\x12\x31\n\x04info\x18\x02 \x01(\x0b\x32#.livekit.proto.VideoFrameBufferInfo\"\xda\x01\n\x13PlanarYuvBufferInfo\x12\x14\n\x0c\x63hroma_width\x18\x01 \x01(\r\x12\x15\n\rchroma_height\x18\x02 \x01(\r\x12\x10\n\x08stride_y\x18\x03 \x01(\r\x12\x10\n\x08stride_u\x18\x04 \x01(\r\x12\x10\n\x08stride_v\x18\x05 \x01(\r\x12\x10\n\x08stride_a\x18\x06 \x01(\r\x12\x12\n\ndata_y_ptr\x18\x07 \x01(\x04\x12\x12\n\ndata_u_ptr\x18\x08 \x01(\x04\x12\x12\n\ndata_v_ptr\x18\t \x01(\x04\x12\x12\n\ndata_a_ptr\x18\n \x01(\x04\"\x92\x01\n\x15\x42iplanarYuvBufferInfo\x12\x14\n\x0c\x63hroma_width\x18\x01 \x01(\r\x12\x15\n\rchroma_height\x18\x02 \x01(\r\x12\x10\n\x08stride_y\x18\x03 \x01(\r\x12\x11\n\tstride_uv\x18\x04 \x01(\r\x12\x12\n\ndata_y_ptr\x18\x05 \x01(\x04\x12\x13\n\x0b\x64\x61ta_uv_ptr\x18\x06 \x01(\x04\"\x12\n\x10NativeBufferInfo\"?\n\x0fVideoStreamInfo\x12,\n\x04type\x18\x01 \x01(\x0e\x32\x1e.livekit.proto.VideoStreamType\"o\n\x10OwnedVideoStream\x12-\n\x06handle\x18\x01 \x01(\x0b\x32\x1d.livekit.proto.FfiOwnedHandle\x12,\n\x04info\x18\x02 \x01(\x0b\x32\x1e.livekit.proto.VideoStreamInfo\"\x9f\x01\n\x10VideoStreamEvent\x12\x15\n\rstream_handle\x18\x01 \x01(\x04\x12;\n\x0e\x66rame_received\x18\x02 \x01(\x0b\x32!.livekit.proto.VideoFrameReceivedH\x00\x12,\n\x03\x65os\x18\x03 \x01(\x0b\x32\x1d.livekit.proto.VideoStreamEOSH\x00\x42\t\n\x07message\"x\n\x12VideoFrameReceived\x12,\n\x05\x66rame\x18\x01 \x01(\x0b\x32\x1d.livekit.proto.VideoFrameInfo\x12\x34\n\x06\x62uffer\x18\x02 \x01(\x0b\x32$.livekit.proto.OwnedVideoFrameBuffer\"\x10\n\x0eVideoStreamEOS\"6\n\x15VideoSourceResolution\x12\r\n\x05width\x18\x01 \x01(\r\x12\x0e\n\x06height\x18\x02 \x01(\r\"?\n\x0fVideoSourceInfo\x12,\n\x04type\x18\x01 \x01(\x0e\x32\x1e.livekit.proto.VideoSourceType\"o\n\x10OwnedVideoSource\x12-\n\x06handle\x18\x01 \x01(\x0b\x32\x1d.livekit.proto.FfiOwnedHandle\x12,\n\x04info\x18\x02 \x01(\x0b\x32\x1e.livekit.proto.VideoSourceInfo*(\n\nVideoCodec\x12\x07\n\x03VP8\x10\x00\x12\x08\n\x04H264\x10\x01\x12\x07\n\x03\x41V1\x10\x02*l\n\rVideoRotation\x12\x14\n\x10VIDEO_ROTATION_0\x10\x00\x12\x15\n\x11VIDEO_ROTATION_90\x10\x01\x12\x16\n\x12VIDEO_ROTATION_180\x10\x02\x12\x16\n\x12VIDEO_ROTATION_270\x10\x03*U\n\x0fVideoFormatType\x12\x0f\n\x0b\x46ORMAT_ARGB\x10\x00\x12\x0f\n\x0b\x46ORMAT_BGRA\x10\x01\x12\x0f\n\x0b\x46ORMAT_ABGR\x10\x02\x12\x0f\n\x0b\x46ORMAT_RGBA\x10\x03*_\n\x14VideoFrameBufferType\x12\n\n\x06NATIVE\x10\x00\x12\x08\n\x04I420\x10\x01\x12\t\n\x05I420A\x10\x02\x12\x08\n\x04I422\x10\x03\x12\x08\n\x04I444\x10\x04\x12\x08\n\x04I010\x10\x05\x12\x08\n\x04NV12\x10\x06*Y\n\x0fVideoStreamType\x12\x17\n\x13VIDEO_STREAM_NATIVE\x10\x00\x12\x16\n\x12VIDEO_STREAM_WEBGL\x10\x01\x12\x15\n\x11VIDEO_STREAM_HTML\x10\x02**\n\x0fVideoSourceType\x12\x17\n\x13VIDEO_SOURCE_NATIVE\x10\x00\x42\x10\xaa\x02\rLiveKit.Protob\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'video_frame_pb2', _globals)
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  DESCRIPTOR._serialized_options = b'\252\002\rLiveKit.Proto'
  _globals['_VIDEOCODEC']._serialized_start=2940
  _globals['_VIDEOCODEC']._serialized_end=2980
  _globals['_VIDEOROTATION']._serialized_start=2982
  _globals['_VIDEOROTATION']._serialized_end=3090
  _globals['_VIDEOFORMATTYPE']._serialized_start=3092
  _globals['_VIDEOFORMATTYPE']._serialized_end=3177
  _globals['_VIDEOFRAMEBUFFERTYPE']._serialized_start=3179
  _globals['_VIDEOFRAMEBUFFERTYPE']._serialized_end=3274
  _globals['_VIDEOSTREAMTYPE']._serialized_start=3276
  _globals['_VIDEOSTREAMTYPE']._serialized_end=3365
  _globals['_VIDEOSOURCETYPE']._serialized_start=3367
  _globals['_VIDEOSOURCETYPE']._serialized_end=3409
  _globals['_ALLOCVIDEOBUFFERREQUEST']._serialized_start=50
  _globals['_ALLOCVIDEOBUFFERREQUEST']._serialized_end=157
  _globals['_ALLOCVIDEOBUFFERRESPONSE']._serialized_start=159
  _globals['_ALLOCVIDEOBUFFERRESPONSE']._serialized_end=239
  _globals['_NEWVIDEOSTREAMREQUEST']._serialized_start=241
  _globals['_NEWVIDEOSTREAMREQUEST']._serialized_end=332
  _globals['_NEWVIDEOSTREAMRESPONSE']._serialized_start=334
  _globals['_NEWVIDEOSTREAMRESPONSE']._serialized_end=407
  _globals['_NEWVIDEOSOURCEREQUEST']._serialized_start=409
  _globals['_NEWVIDEOSOURCEREQUEST']._serialized_end=536
  _globals['_NEWVIDEOSOURCERESPONSE']._serialized_start=538
  _globals['_NEWVIDEOSOURCERESPONSE']._serialized_end=611
  _globals['_CAPTUREVIDEOFRAMEREQUEST']._serialized_start=613
  _globals['_CAPTUREVIDEOFRAMEREQUEST']._serialized_end=731
  _globals['_CAPTUREVIDEOFRAMERESPONSE']._serialized_start=733
  _globals['_CAPTUREVIDEOFRAMERESPONSE']._serialized_end=760
  _globals['_TOI420REQUEST']._serialized_start=762
  _globals['_TOI420REQUEST']._serialized_end=870
  _globals['_TOI420RESPONSE']._serialized_start=872
  _globals['_TOI420RESPONSE']._serialized_end=942
  _globals['_TOARGBREQUEST']._serialized_start=945
  _globals['_TOARGBREQUEST']._serialized_end=1127
  _globals['_TOARGBRESPONSE']._serialized_start=1129
  _globals['_TOARGBRESPONSE']._serialized_end=1145
  _globals['_VIDEORESOLUTION']._serialized_start=1147
  _globals['_VIDEORESOLUTION']._serialized_end=1215
  _globals['_ARGBBUFFERINFO']._serialized_start=1217
  _globals['_ARGBBUFFERINFO']._serialized_end=1341
  _globals['_VIDEOFRAMEINFO']._serialized_start=1343
  _globals['_VIDEOFRAMEINFO']._serialized_end=1429
  _globals['_VIDEOFRAMEBUFFERINFO']._serialized_start=1432
  _globals['_VIDEOFRAMEBUFFERINFO']._serialized_end=1711
  _globals['_OWNEDVIDEOFRAMEBUFFER']._serialized_start=1713
  _globals['_OWNEDVIDEOFRAMEBUFFER']._serialized_end=1834
  _globals['_PLANARYUVBUFFERINFO']._serialized_start=1837
  _globals['_PLANARYUVBUFFERINFO']._serialized_end=2055
  _globals['_BIPLANARYUVBUFFERINFO']._serialized_start=2058
  _globals['_BIPLANARYUVBUFFERINFO']._serialized_end=2204
  _globals['_NATIVEBUFFERINFO']._serialized_start=2206
  _globals['_NATIVEBUFFERINFO']._serialized_end=2224
  _globals['_VIDEOSTREAMINFO']._serialized_start=2226
  _globals['_VIDEOSTREAMINFO']._serialized_end=2289
  _globals['_OWNEDVIDEOSTREAM']._serialized_start=2291
  _globals['_OWNEDVIDEOSTREAM']._serialized_end=2402
  _globals['_VIDEOSTREAMEVENT']._serialized_start=2405
  _globals['_VIDEOSTREAMEVENT']._serialized_end=2564
  _globals['_VIDEOFRAMERECEIVED']._serialized_start=2566
  _globals['_VIDEOFRAMERECEIVED']._serialized_end=2686
  _globals['_VIDEOSTREAMEOS']._serialized_start=2688
  _globals['_VIDEOSTREAMEOS']._serialized_end=2704
  _globals['_VIDEOSOURCERESOLUTION']._serialized_start=2706
  _globals['_VIDEOSOURCERESOLUTION']._serialized_end=2760
  _globals['_VIDEOSOURCEINFO']._serialized_start=2762
  _globals['_VIDEOSOURCEINFO']._serialized_end=2825
  _globals['_OWNEDVIDEOSOURCE']._serialized_start=2827
  _globals['_OWNEDVIDEOSOURCE']._serialized_end=2938
# @@protoc_insertion_point(module_scope)
