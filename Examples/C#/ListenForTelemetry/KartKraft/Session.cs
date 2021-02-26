// <auto-generated>
//  automatically generated by the FlatBuffers compiler, do not modify
// </auto-generated>

namespace KartKraft
{

using global::System;
using global::System.Collections.Generic;
using global::FlatBuffers;

/// Session data
public struct Session : IFlatbufferObject
{
  private Table __p;
  public ByteBuffer ByteBuffer { get { return __p.bb; } }
  public static void ValidateVersion() { FlatBufferConstants.FLATBUFFERS_1_12_0(); }
  public static Session GetRootAsSession(ByteBuffer _bb) { return GetRootAsSession(_bb, new Session()); }
  public static Session GetRootAsSession(ByteBuffer _bb, Session obj) { return (obj.__assign(_bb.GetInt(_bb.Position) + _bb.Position, _bb)); }
  public void __init(int _i, ByteBuffer _bb) { __p = new Table(_i, _bb); }
  public Session __assign(int _i, ByteBuffer _bb) { __init(_i, _bb); return this; }

  public KartKraft.Vehicle? Vehicles(int j) { int o = __p.__offset(10); return o != 0 ? (KartKraft.Vehicle?)(new KartKraft.Vehicle()).__assign(__p.__indirect(__p.__vector(o) + j * 4), __p.bb) : null; }
  public int VehiclesLength { get { int o = __p.__offset(10); return o != 0 ? __p.__vector_len(o) : 0; } }
  public float TimeElapsed { get { int o = __p.__offset(12); return o != 0 ? __p.bb.GetFloat(o + __p.bb_pos) : (float)0.0f; } }

  public static Offset<KartKraft.Session> CreateSession(FlatBufferBuilder builder,
      VectorOffset vehiclesOffset = default(VectorOffset),
      float timeElapsed = 0.0f) {
    builder.StartTable(5);
    Session.AddTimeElapsed(builder, timeElapsed);
    Session.AddVehicles(builder, vehiclesOffset);
    return Session.EndSession(builder);
  }

  public static void StartSession(FlatBufferBuilder builder) { builder.StartTable(5); }
  public static void AddVehicles(FlatBufferBuilder builder, VectorOffset vehiclesOffset) { builder.AddOffset(3, vehiclesOffset.Value, 0); }
  public static VectorOffset CreateVehiclesVector(FlatBufferBuilder builder, Offset<KartKraft.Vehicle>[] data) { builder.StartVector(4, data.Length, 4); for (int i = data.Length - 1; i >= 0; i--) builder.AddOffset(data[i].Value); return builder.EndVector(); }
  public static VectorOffset CreateVehiclesVectorBlock(FlatBufferBuilder builder, Offset<KartKraft.Vehicle>[] data) { builder.StartVector(4, data.Length, 4); builder.Add(data); return builder.EndVector(); }
  public static void StartVehiclesVector(FlatBufferBuilder builder, int numElems) { builder.StartVector(4, numElems, 4); }
  public static void AddTimeElapsed(FlatBufferBuilder builder, float timeElapsed) { builder.AddFloat(4, timeElapsed, 0.0f); }
  public static Offset<KartKraft.Session> EndSession(FlatBufferBuilder builder) {
    int o = builder.EndTable();
    return new Offset<KartKraft.Session>(o);
  }
};


}
