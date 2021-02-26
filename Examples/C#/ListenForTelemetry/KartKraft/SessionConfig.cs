// <auto-generated>
//  automatically generated by the FlatBuffers compiler, do not modify
// </auto-generated>

namespace KartKraft
{

using global::System;
using global::System.Collections.Generic;
using global::FlatBuffers;

public struct SessionConfig : IFlatbufferObject
{
  private Table __p;
  public ByteBuffer ByteBuffer { get { return __p.bb; } }
  public static void ValidateVersion() { FlatBufferConstants.FLATBUFFERS_1_12_0(); }
  public static SessionConfig GetRootAsSessionConfig(ByteBuffer _bb) { return GetRootAsSessionConfig(_bb, new SessionConfig()); }
  public static SessionConfig GetRootAsSessionConfig(ByteBuffer _bb, SessionConfig obj) { return (obj.__assign(_bb.GetInt(_bb.Position) + _bb.Position, _bb)); }
  public void __init(int _i, ByteBuffer _bb) { __p = new Table(_i, _bb); }
  public SessionConfig __assign(int _i, ByteBuffer _bb) { __init(_i, _bb); return this; }

  public string Name { get { int o = __p.__offset(4); return o != 0 ? __p.__string(o + __p.bb_pos) : null; } }
#if ENABLE_SPAN_T
  public Span<byte> GetNameBytes() { return __p.__vector_as_span<byte>(4, 1); }
#else
  public ArraySegment<byte>? GetNameBytes() { return __p.__vector_as_arraysegment(4); }
#endif
  public byte[] GetNameArray() { return __p.__vector_as_array<byte>(4); }
  public uint TimeLimit { get { int o = __p.__offset(6); return o != 0 ? __p.bb.GetUint(o + __p.bb_pos) : (uint)0; } }
  public uint LapLimit { get { int o = __p.__offset(8); return o != 0 ? __p.bb.GetUint(o + __p.bb_pos) : (uint)0; } }

  public static Offset<KartKraft.SessionConfig> CreateSessionConfig(FlatBufferBuilder builder,
      StringOffset nameOffset = default(StringOffset),
      uint timeLimit = 0,
      uint lapLimit = 0) {
    builder.StartTable(3);
    SessionConfig.AddLapLimit(builder, lapLimit);
    SessionConfig.AddTimeLimit(builder, timeLimit);
    SessionConfig.AddName(builder, nameOffset);
    return SessionConfig.EndSessionConfig(builder);
  }

  public static void StartSessionConfig(FlatBufferBuilder builder) { builder.StartTable(3); }
  public static void AddName(FlatBufferBuilder builder, StringOffset nameOffset) { builder.AddOffset(0, nameOffset.Value, 0); }
  public static void AddTimeLimit(FlatBufferBuilder builder, uint timeLimit) { builder.AddUint(1, timeLimit, 0); }
  public static void AddLapLimit(FlatBufferBuilder builder, uint lapLimit) { builder.AddUint(2, lapLimit, 0); }
  public static Offset<KartKraft.SessionConfig> EndSessionConfig(FlatBufferBuilder builder) {
    int o = builder.EndTable();
    return new Offset<KartKraft.SessionConfig>(o);
  }
};


}
