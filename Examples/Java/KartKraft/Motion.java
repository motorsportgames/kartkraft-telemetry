// automatically generated by the FlatBuffers compiler, do not modify

package KartKraft;

import java.nio.*;
import java.lang.*;
import java.util.*;
import com.google.flatbuffers.*;

@SuppressWarnings("unused")
/**
 * Motion data of local player for driving hardware motion simulators
 */
public final class Motion extends Table {
  public static Motion getRootAsMotion(ByteBuffer _bb) { return getRootAsMotion(_bb, new Motion()); }
  public static Motion getRootAsMotion(ByteBuffer _bb, Motion obj) { _bb.order(ByteOrder.LITTLE_ENDIAN); return (obj.__assign(_bb.getInt(_bb.position()) + _bb.position(), _bb)); }
  public void __init(int _i, ByteBuffer _bb) { bb_pos = _i; bb = _bb; }
  public Motion __assign(int _i, ByteBuffer _bb) { __init(_i, _bb); return this; }

  public float pitch() { int o = __offset(4); return o != 0 ? bb.getFloat(o + bb_pos) : 0.0f; }
  public float roll() { int o = __offset(6); return o != 0 ? bb.getFloat(o + bb_pos) : 0.0f; }
  public float yaw() { int o = __offset(8); return o != 0 ? bb.getFloat(o + bb_pos) : 0.0f; }
  public float accelerationX() { int o = __offset(10); return o != 0 ? bb.getFloat(o + bb_pos) : 0.0f; }
  public float accelerationY() { int o = __offset(12); return o != 0 ? bb.getFloat(o + bb_pos) : 0.0f; }
  public float accelerationZ() { int o = __offset(14); return o != 0 ? bb.getFloat(o + bb_pos) : 0.0f; }
  public float traction() { int o = __offset(16); return o != 0 ? bb.getFloat(o + bb_pos) : 0.0f; }

  public static int createMotion(FlatBufferBuilder builder,
      float pitch,
      float roll,
      float yaw,
      float accelerationX,
      float accelerationY,
      float accelerationZ,
      float traction) {
    builder.startObject(7);
    Motion.addTraction(builder, traction);
    Motion.addAccelerationZ(builder, accelerationZ);
    Motion.addAccelerationY(builder, accelerationY);
    Motion.addAccelerationX(builder, accelerationX);
    Motion.addYaw(builder, yaw);
    Motion.addRoll(builder, roll);
    Motion.addPitch(builder, pitch);
    return Motion.endMotion(builder);
  }

  public static void startMotion(FlatBufferBuilder builder) { builder.startObject(7); }
  public static void addPitch(FlatBufferBuilder builder, float pitch) { builder.addFloat(0, pitch, 0.0f); }
  public static void addRoll(FlatBufferBuilder builder, float roll) { builder.addFloat(1, roll, 0.0f); }
  public static void addYaw(FlatBufferBuilder builder, float yaw) { builder.addFloat(2, yaw, 0.0f); }
  public static void addAccelerationX(FlatBufferBuilder builder, float accelerationX) { builder.addFloat(3, accelerationX, 0.0f); }
  public static void addAccelerationY(FlatBufferBuilder builder, float accelerationY) { builder.addFloat(4, accelerationY, 0.0f); }
  public static void addAccelerationZ(FlatBufferBuilder builder, float accelerationZ) { builder.addFloat(5, accelerationZ, 0.0f); }
  public static void addTraction(FlatBufferBuilder builder, float traction) { builder.addFloat(6, traction, 0.0f); }
  public static int endMotion(FlatBufferBuilder builder) {
    int o = builder.endObject();
    return o;
  }
}

