
TASK_METRICS_VIEW_CONFIG = {
  'hdfs': {
    'journalnode':[
      ('Rpc', [
        [('JournalNode', 'ReceivedBytes', 'byte(s)')],
        [('JournalNode', 'SentBytes', 'byte(s)')],
        [('JournalNode', 'RpcQueueTimeNumOps', 'op(s)')],
        [('JournalNode', 'RpcQueueTimeAvgTime', 'ms(s)')],
      ]),
    ],
    'namenode':[
      # view
      ('Overall', [
        # graph
        # TODO:support comparison multi-metric in one graph
        [('NameNode', 'BlockCapacity', 'block(s)')],
        [('NameNode', 'BlocksTotal', 'block(s)')],
        [('NameNode', 'CapacityRemainingGB', 'GB')],
        [('NameNode', 'CapacityTotalGB', 'GB')],
        [('NameNode', 'CapacityUsedGB', 'GB')],
        [('NameNode', 'CorruptBlocks', 'block(s)')],
        [('NameNode', 'ExcessBlocks', 'block(s)')],
        [('NameNode', 'FilesTotal', 'file(s)')],
      ]),
      ('Operation', [
        [('NameNode', 'AddBlockOps', 'op(s)')],
        [('NameNode', 'CreateFileOps', 'op(s)')],
        [('NameNode', 'DeleteFileOps', 'op(s)')],
        [('NameNode', 'FileInfoOps', 'op(s)')],
        [('NameNode', 'GetListingOps', 'op(s)')],
      ]),
      ('Rpc', [
        [('NameNode', 'ReceivedBytes', 'byte(s)')],
        [('NameNode', 'SentBytes', 'byte(s)')],
        [('NameNode', 'RpcQueueTimeNumOps', 'op(s)')],
        [('NameNode', 'RpcQueueTimeAvgTime', 'ms(s)')],
      ]
      )
    ],
    'datanode':[
      ('BlockOperation', [
        [('DataNode', 'BlockReportsAvgTime', 'ms(s)')],
        [('DataNode', 'BlockReportsNumOps', 'op(s)')],
        [('DataNode', 'BlocksGetLocalPathInfo', '')],
        [('DataNode', 'BlocksRead', 'block(s)')],
        [('DataNode', 'BlocksRemoved', 'block(s)')],
        [('DataNode', 'BlocksReplicated', 'block(s)')],
        [('DataNode', 'BlocksVerified', 'block(s)')],
        [('DataNode', 'BlocksWritten', 'block(s)')],
      ]),
      ('Activity', [
        [('DataNode', 'BytesWritten', '')],
        [('DataNode', 'BytesRead', '')],
        [('DataNode', 'BlocksWritten', '')],
        [('DataNode', 'BlocksRead', '')],
        [('DataNode', 'BlocksReplicated', '')],
        [('DataNode', 'BlocksRemoved', '')],
        [('DataNode', 'BlocksVerified', '')],
        [('DataNode', 'BlockVerificationFailures', '')],
        [('DataNode', 'ReadsFromLocalClient', '')],
        [('DataNode', 'ReadsFromRemoteClient', '')],
        [('DataNode', 'WritesFromLocalClient', '')],
        [('DataNode', 'WritesFromRemoteClient', '')],
        [('DataNode', 'BlocksGetLocalPathInfo', '')],
        [('DataNode', 'FsyncCount', '')],
        [('DataNode', 'VolumeFailures', '')],
        [('DataNode', 'ReadBlockOpNumOps', '')],
        [('DataNode', 'ReadBlockOpAvgTime', '')],
        [('DataNode', 'WriteBlockOpNumOps', '')],
        [('DataNode', 'WriteBlockOpAvgTime', '')],
        [('DataNode', 'BlockChecksumOpNumOps', '')],
        [('DataNode', 'BlockChecksumOpAvgTime', '')],
        [('DataNode', 'CopyBlockOpNumOps', '')],
        [('DataNode', 'CopyBlockOpAvgTime', '')],
        [('DataNode', 'ReplaceBlockOpNumOps', '')],
        [('DataNode', 'ReplaceBlockOpAvgTime', '')],
        [('DataNode', 'HeartbeatsNumOps', '')],
        [('DataNode', 'HeartbeatsAvgTime', '')],
        [('DataNode', 'BlockReportsNumOps', '')],
        [('DataNode', 'BlockReportsAvgTime', '')],
        [('DataNode', 'PacketAckRoundTripTimeNanosNumOps', '')],
        [('DataNode', 'PacketAckRoundTripTimeNanosAvgTime', '')],
        [('DataNode', 'FlushNanosNumOps', '')],
        [('DataNode', 'FlushNanosAvgTime', '')],
        [('DataNode', 'FsyncNanosNumOps', '')],
        [('DataNode', 'FsyncNanosAvgTime', '')],
        [('DataNode', 'SendDataPacketBlockedOnNetworkNanosNumOps', '')],
        [('DataNode', 'SendDataPacketBlockedOnNetworkNanosAvgTime', '')],
        [('DataNode', 'SendDataPacketTransferNanosNumOps', '')],
        [('DataNode', 'SendDataPacketTransferNanosAvgTime', '')],
        [('DataNode', 'PacketAckRoundTripTimeNanos60sNumOps', '')],
        [('DataNode', 'PacketAckRoundTripTimeNanos60s50thPercentileLatency', '')],
        [('DataNode', 'PacketAckRoundTripTimeNanos60s75thPercentileLatency', '')],
        [('DataNode', 'PacketAckRoundTripTimeNanos60s90thPercentileLatency', '')],
        [('DataNode', 'PacketAckRoundTripTimeNanos60s95thPercentileLatency', '')],
        [('DataNode', 'PacketAckRoundTripTimeNanos60s99thPercentileLatency', '')],
        [('DataNode', 'PacketAckRoundTripTimeNanos300sNumOps', '')],
        [('DataNode', 'PacketAckRoundTripTimeNanos300s50thPercentileLatency', '')],
        [('DataNode', 'PacketAckRoundTripTimeNanos300s75thPercentileLatency', '')],
        [('DataNode', 'PacketAckRoundTripTimeNanos300s90thPercentileLatency', '')],
        [('DataNode', 'PacketAckRoundTripTimeNanos300s95thPercentileLatency', '')],
        [('DataNode', 'PacketAckRoundTripTimeNanos300s99thPercentileLatency', '')],
        [('DataNode', 'PacketAckRoundTripTimeNanos900sNumOps', '')],
        [('DataNode', 'PacketAckRoundTripTimeNanos900s50thPercentileLatency', '')],
        [('DataNode', 'PacketAckRoundTripTimeNanos900s75thPercentileLatency', '')],
        [('DataNode', 'PacketAckRoundTripTimeNanos900s90thPercentileLatency', '')],
        [('DataNode', 'PacketAckRoundTripTimeNanos900s95thPercentileLatency', '')],
        [('DataNode', 'PacketAckRoundTripTimeNanos900s99thPercentileLatency', '')],
        [('DataNode', 'FlushNanos60sNumOps', '')],
        [('DataNode', 'FlushNanos60s50thPercentileLatency', '')],
        [('DataNode', 'FlushNanos60s75thPercentileLatency', '')],
        [('DataNode', 'FlushNanos60s90thPercentileLatency', '')],
        [('DataNode', 'FlushNanos60s95thPercentileLatency', '')],
        [('DataNode', 'FlushNanos60s99thPercentileLatency', '')],
        [('DataNode', 'FlushNanos300sNumOps', '')],
        [('DataNode', 'FlushNanos300s50thPercentileLatency', '')],
        [('DataNode', 'FlushNanos300s75thPercentileLatency', '')],
        [('DataNode', 'FlushNanos300s90thPercentileLatency', '')],
        [('DataNode', 'FlushNanos300s95thPercentileLatency', '')],
        [('DataNode', 'FlushNanos300s99thPercentileLatency', '')],
        [('DataNode', 'FlushNanos900sNumOps', '')],
        [('DataNode', 'FlushNanos900s50thPercentileLatency', '')],
        [('DataNode', 'FlushNanos900s75thPercentileLatency', '')],
        [('DataNode', 'FlushNanos900s90thPercentileLatency', '')],
        [('DataNode', 'FlushNanos900s95thPercentileLatency', '')],
        [('DataNode', 'FlushNanos900s99thPercentileLatency', '')],
        [('DataNode', 'FsyncNanos60sNumOps', '')],
        [('DataNode', 'FsyncNanos60s50thPercentileLatency', '')],
        [('DataNode', 'FsyncNanos60s75thPercentileLatency', '')],
        [('DataNode', 'FsyncNanos60s90thPercentileLatency', '')],
        [('DataNode', 'FsyncNanos60s95thPercentileLatency', '')],
        [('DataNode', 'FsyncNanos60s99thPercentileLatency', '')],
        [('DataNode', 'FsyncNanos300sNumOps', '')],
        [('DataNode', 'FsyncNanos300s50thPercentileLatency', '')],
        [('DataNode', 'FsyncNanos300s75thPercentileLatency', '')],
        [('DataNode', 'FsyncNanos300s90thPercentileLatency', '')],
        [('DataNode', 'FsyncNanos300s95thPercentileLatency', '')],
        [('DataNode', 'FsyncNanos300s99thPercentileLatency', '')],
        [('DataNode', 'FsyncNanos900sNumOps', '')],
        [('DataNode', 'FsyncNanos900s50thPercentileLatency', '')],
        [('DataNode', 'FsyncNanos900s75thPercentileLatency', '')],
        [('DataNode', 'FsyncNanos900s90thPercentileLatency', '')],
        [('DataNode', 'FsyncNanos900s95thPercentileLatency', '')],
        [('DataNode', 'FsyncNanos900s99thPercentileLatency', '')],
        [('DataNode', 'SendDataPacketBlockedOnNetworkNanos60sNumOps', '')],
        [('DataNode', 'SendDataPacketBlockedOnNetworkNanos60s50thPercentileLatency', '')],
        [('DataNode', 'SendDataPacketBlockedOnNetworkNanos60s75thPercentileLatency', '')],
        [('DataNode', 'SendDataPacketBlockedOnNetworkNanos60s90thPercentileLatency', '')],
        [('DataNode', 'SendDataPacketBlockedOnNetworkNanos60s95thPercentileLatency', '')],
        [('DataNode', 'SendDataPacketBlockedOnNetworkNanos60s99thPercentileLatency', '')],
        [('DataNode', 'SendDataPacketBlockedOnNetworkNanos300sNumOps', '')],
        [('DataNode', 'SendDataPacketBlockedOnNetworkNanos300s50thPercentileLatency', '')],
        [('DataNode', 'SendDataPacketBlockedOnNetworkNanos300s75thPercentileLatency', '')],
        [('DataNode', 'SendDataPacketBlockedOnNetworkNanos300s90thPercentileLatency', '')],
        [('DataNode', 'SendDataPacketBlockedOnNetworkNanos300s95thPercentileLatency', '')],
        [('DataNode', 'SendDataPacketBlockedOnNetworkNanos300s99thPercentileLatency', '')],
        [('DataNode', 'SendDataPacketBlockedOnNetworkNanos900sNumOps', '')],
        [('DataNode', 'SendDataPacketBlockedOnNetworkNanos900s50thPercentileLatency', '')],
        [('DataNode', 'SendDataPacketBlockedOnNetworkNanos900s75thPercentileLatency', '')],
        [('DataNode', 'SendDataPacketBlockedOnNetworkNanos900s90thPercentileLatency', '')],
        [('DataNode', 'SendDataPacketBlockedOnNetworkNanos900s95thPercentileLatency', '')],
        [('DataNode', 'SendDataPacketBlockedOnNetworkNanos900s99thPercentileLatency', '')],
        [('DataNode', 'SendDataPacketTransferNanos60sNumOps', '')],
        [('DataNode', 'SendDataPacketTransferNanos60s50thPercentileLatency', '')],
        [('DataNode', 'SendDataPacketTransferNanos60s75thPercentileLatency', '')],
        [('DataNode', 'SendDataPacketTransferNanos60s90thPercentileLatency', '')],
        [('DataNode', 'SendDataPacketTransferNanos60s95thPercentileLatency', '')],
        [('DataNode', 'SendDataPacketTransferNanos60s99thPercentileLatency', '')],
        [('DataNode', 'SendDataPacketTransferNanos300sNumOps', '')],
        [('DataNode', 'SendDataPacketTransferNanos300s50thPercentileLatency', '')],
        [('DataNode', 'SendDataPacketTransferNanos300s75thPercentileLatency', '')],
        [('DataNode', 'SendDataPacketTransferNanos300s90thPercentileLatency', '')],
        [('DataNode', 'SendDataPacketTransferNanos300s95thPercentileLatency', '')],
        [('DataNode', 'SendDataPacketTransferNanos300s99thPercentileLatency', '')],
        [('DataNode', 'SendDataPacketTransferNanos900sNumOps', '')],
        [('DataNode', 'SendDataPacketTransferNanos900s50thPercentileLatency', '')],
        [('DataNode', 'SendDataPacketTransferNanos900s75thPercentileLatency', '')],
        [('DataNode', 'SendDataPacketTransferNanos900s90thPercentileLatency', '')],
        [('DataNode', 'SendDataPacketTransferNanos900s95thPercentileLatency', '')],
        [('DataNode', 'SendDataPacketTransferNanos900s99thPercentileLatency', '')],
      ]),
    ],
  },
  'hbase' : {
    'master':[
      ('Operation', [
        [('HBase', 'putNumOps', 'op(s)')],
        [('HBase', 'putAvgTime', 'us(s)')],
        [('HBase', 'checkAndPutNumOps', 'op(s)')],
        [('HBase', 'checkAndPutAvgTime', 'us(s)')],
        [('HBase', 'getNumOps', 'op(s)')],
        [('HBase', 'getAvgTime', 'us(s)')],
        [('HBase', 'deleteNumOps', 'op(s)')],
        [('HBase', 'deleteAvgTime', 'us(s)')],
      ]),
      ('RPC', [
        [('HBase', 'RpcQueueTimeNumOps', 'op(s)')],
        [('HBase', 'RpcQueueTimeAvgTime', 'ms(s)')],
        [('HBase', 'RpcProcessingTimeNumOps', 'op(s)')],
        [('HBase', 'RpcProcessingTimeAvgTime', 'us(s)')],
        [('HBase', 'RpcSlowResponseNumOps', 'op(s)')],
        [('HBase', 'RpcSlowResponseAvgTime', 'ms(s)')],
      ]),
      ('JvmStatistics', [
        [('Master', 'memHeapCommittedM', 'MB')],
        [('Master', 'fatalCount', 'count(s)')],
        [('Master', 'threadsWaiting', 'thread(s)')],
        [('Master', 'threadsBlocked', 'thread(s)')],
        [('Master', 'gcCount', 'count(s)')],
        [('Master', 'errorCount', 'count(s)')],
        [('Master', 'memNonHeapCommittedM', 'MB')],
        [('Master', 'warnCount', 'count(s)')],
        [('Master', 'gcTimeMillis', 'ms(s)')],
        [('Master', 'memNonHeapUsedM', 'MB')],
        [('Master', 'memHeapUsedM', 'MB')],
        [('Master', 'threadsNew', 'thread(s)')],
        [('Master', 'threadsTerminated', 'thread(s)')],
        [('Master', 'threadsTimedWaiting', 'thread(s)')],
        [('Master', 'maxMemoryM', 'MB')],
        [('Master', 'infoCount', 'count(s)')],
        [('Master', 'threadsRunnable', 'thread(s)')],
      ]),
    ],
    'regionserver': [
      ('Operation', [
        [('HBase', 'multiNumOps', 'op(s)')],
        [('HBase', 'multiAvgTime', 'us(s)')],
        [('HBase', 'checkAndPutNumOps', 'op(s)')],
        [('HBase', 'checkAndPutAvgTime', 'us(s)')],
        [('HBase', 'getNumOps', 'op(s)')],
        [('HBase', 'getAvgTime', 'us(s)')],
        [('HBase', 'openScannerNumOps', 'op(s)')],
        [('HBase', 'openScannerAvgTime', 'us(s)')],
        [('HBase', 'nextNumOps', 'op(s)')],
        [('HBase', 'nextAvgTime', 'us(s)')],
        [('HBase', 'deleteNumOps', 'op(s)')],
        [('HBase', 'deleteAvgTime', 'us(s)')],
      ]),
      ('RPC', [
        [('HBase', 'RpcQueueTimeNumOps', 'op(s)')],
        [('HBase', 'RpcQueueTimeAvgTime', 'ms(s)')],
        [('HBase', 'RpcProcessingTimeNumOps', 'op(s)')],
        [('HBase', 'RpcProcessingTimeAvgTime', 'us(s)')],
        [('HBase', 'RpcSlowResponseNumOps', 'op(s)')],
        [('HBase', 'RpcSlowResponseAvgTime', 'ms(s)')],
      ]),
      ('Store', [
        [('RegionServer', 'regions', 'region(s)')],
        [('RegionServer', 'memstoreSizeMB', 'MB')],
        [('RegionServer', 'storefileIndexSizeMB', 'MB')],
        [('RegionServer', 'storeFileSizeMB', 'MB')],
        [('RegionServer', 'storefiles', 'file(s)')],
        [('RegionServer', 'stores', 'store(s)')],
        [('RegionServer', 'largeCompactionQueueSize', 'count(s)')],
        [('RegionServer', 'smallCompactionQueueSize', 'count(s)')],
        [('RegionServer', 'compactionTime', 'ms(s)')],
        [('RegionServer', 'compactionSize', 'byte(s)')],
        [('RegionServer', 'flushQueueSize', 'count(s)')],
        [('RegionServer', 'flushTime', 'second(s)')],
        [('RegionServer', 'flushSize', 'byte(s)')],
        [('RegionServer', 'hlogRollCount', 'count(s)')],
      ]),
      ('BlockCache', [
        [('RegionServer', 'blockCacheCount', 'count(s)')],
        [('RegionServer', 'blockCacheFree', 'byte(s)')],
        [('RegionServer', 'blockCacheHitRatio', '%')],
        [('RegionServer', 'blockCacheHitCount', 'count(s)')],
        [('RegionServer', 'blockCacheMissCount', 'count(s)')],
        [('RegionServer', 'blockCacheSize', 'byte(s)' )],
      ]),
      ('FileSystem', [
        [('RegionServer', 'fsReadLatencyNumOps', 'op(s)')],
        [('RegionServer', 'fsReadLatencyAvgTime', 'ms(s)')],
        [('RegionServer', 'fsPreadLatencyNumOps', 'op(s)')],
        [('RegionServer', 'fsPreadLatencyAvgTime', 'ms(s)')],
        [('RegionServer', 'fsWriteLatencyNumOps', 'op(s)')],
        [('RegionServer', 'fsWriteLatencyAvgTime', 'ms(s)')],
        [('RegionServer', 'fsSyncLatencyNumOps', 'op(s)')],
        [('RegionServer', 'fsSyncLatencyAvgTime', 'ms(s)')],
      ]),
      ('JvmStatistics', [
        [('RegionServer', 'memHeapCommittedM', 'MB')],
        [('RegionServer', 'fatalCount', 'count(s)')],
        [('RegionServer', 'threadsWaiting', 'thread(s)')],
        [('RegionServer', 'threadsBlocked', 'thread(s)')],
        [('RegionServer', 'gcCount', 'count(s)')],
        [('RegionServer', 'errorCount', 'count(s)')],
        [('RegionServer', 'memNonHeapCommittedM', 'MB')],
        [('RegionServer', 'warnCount', 'count(s)')],
        [('RegionServer', 'gcTimeMillis', 'ms(s)')],
        [('RegionServer', 'memNonHeapUsedM', 'MB')],
        [('RegionServer', 'memHeapUsedM', 'MB')],
        [('RegionServer', 'threadsNew', 'thread(s)')],
        [('RegionServer', 'threadsTerminated', 'thread(s)')],
        [('RegionServer', 'threadsTimedWaiting', 'thread(s)')],
        [('RegionServer', 'maxMemoryM', 'MB')],
        [('RegionServer', 'infoCount', 'count(s)')],
        [('RegionServer', 'threadsRunnable', 'thread(s)')],
      ]),
    ],
  }
}

JOB_METRICS_VIEW_CONFIG = {
  'hdfs': {
    'journalnode':[
      ('Rpc', [
        [('JournalNode', 'ReceivedBytes', 'byte(s)')],
        [('JournalNode', 'SentBytes', 'byte(s)')],
        [('JournalNode', 'RpcQueueTimeNumOps', 'req(s)')],
        [('JournalNode', 'RpcQueueTimeAvgTime', 'ms(s)')],
      ]),
    ],
    'namenode':[
      # view
      ('Overall', [
        # graph
        [('NameNode', 'BlockCapacity', 'block(s)')],
        [('NameNode', 'BlocksTotal', 'block(s)')],
        [('NameNode', 'CapacityRemainingGB', 'GB')],
        [('NameNode', 'CapacityTotalGB', 'GB')],
        [('NameNode', 'CapacityUsedGB', 'GB')],
        [('NameNode', 'CorruptBlocks', 'block(s)')],
        [('NameNode', 'ExcessBlocks', 'block(s)')],
        [('NameNode', 'FilesTotal', 'file(s)')],
      ]),
      ('Operation', [
        [('NameNode', 'AddBlockOps', 'op(s)')],
        [('NameNode', 'CreateFileOps', 'op(s)')],
        [('NameNode', 'DeleteFileOps', 'op(s)')],
        [('NameNode', 'FileInfoOps', 'op(s)')],
        [('NameNode', 'GetListingOps', 'op(s)')],
      ]),
      ('Rpc', [
        [('NameNode', 'ReceivedBytes', 'byte(s)')],
        [('NameNode', 'SentBytes', 'byte(s)')],
        [('NameNode', 'RpcQueueTimeNumOps', 'op(s)')],
        [('NameNode', 'RpcQueueTimeAvgTime', 'ms(s)')],
      ]
      )
    ],
    'datanode':[
      ('BlockOperation', [
        [('DataNode', 'BlockReportsAvgTime', 'ms(s)')],
        [('DataNode', 'BlockReportsNumOps', 'op(s)')],
        [('DataNode', 'BlocksGetLocalPathInfo', '')],
        [('DataNode', 'BlocksRead', 'block(s)')],
        [('DataNode', 'BlocksRemoved', 'block(s)')],
        [('DataNode', 'BlocksReplicated', 'block(s)')],
        [('DataNode', 'BlocksVerified', 'block(s)')],
        [('DataNode', 'BlocksWritten', 'block(s)')],
      ]),
      ('Activity', [
        [('DataNode', 'BytesWritten', '')],
        [('DataNode', 'BytesRead', '')],
        [('DataNode', 'BlocksWritten', '')],
        [('DataNode', 'BlocksRead', '')],
        [('DataNode', 'BlocksReplicated', '')],
        [('DataNode', 'BlocksRemoved', '')],
        [('DataNode', 'BlocksVerified', '')],
        [('DataNode', 'BlockVerificationFailures', '')],
        [('DataNode', 'ReadsFromLocalClient', '')],
        [('DataNode', 'ReadsFromRemoteClient', '')],
        [('DataNode', 'WritesFromLocalClient', '')],
        [('DataNode', 'WritesFromRemoteClient', '')],
        [('DataNode', 'BlocksGetLocalPathInfo', '')],
        [('DataNode', 'FsyncCount', '')],
        [('DataNode', 'VolumeFailures', '')],
        [('DataNode', 'ReadBlockOpNumOps', '')],
        [('DataNode', 'ReadBlockOpAvgTime', '')],
        [('DataNode', 'WriteBlockOpNumOps', '')],
        [('DataNode', 'WriteBlockOpAvgTime', '')],
        [('DataNode', 'BlockChecksumOpNumOps', '')],
        [('DataNode', 'BlockChecksumOpAvgTime', '')],
        [('DataNode', 'CopyBlockOpNumOps', '')],
        [('DataNode', 'CopyBlockOpAvgTime', '')],
        [('DataNode', 'ReplaceBlockOpNumOps', '')],
        [('DataNode', 'ReplaceBlockOpAvgTime', '')],
        [('DataNode', 'HeartbeatsNumOps', '')],
        [('DataNode', 'HeartbeatsAvgTime', '')],
        [('DataNode', 'BlockReportsNumOps', '')],
        [('DataNode', 'BlockReportsAvgTime', '')],
        [('DataNode', 'PacketAckRoundTripTimeNanosNumOps', '')],
        [('DataNode', 'PacketAckRoundTripTimeNanosAvgTime', '')],
        [('DataNode', 'FlushNanosNumOps', '')],
        [('DataNode', 'FlushNanosAvgTime', '')],
        [('DataNode', 'FsyncNanosNumOps', '')],
        [('DataNode', 'FsyncNanosAvgTime', '')],
        [('DataNode', 'SendDataPacketBlockedOnNetworkNanosNumOps', '')],
        [('DataNode', 'SendDataPacketBlockedOnNetworkNanosAvgTime', '')],
        [('DataNode', 'SendDataPacketTransferNanosNumOps', '')],
        [('DataNode', 'SendDataPacketTransferNanosAvgTime', '')],
        [('DataNode', 'PacketAckRoundTripTimeNanos60sNumOps', '')],
        [('DataNode', 'PacketAckRoundTripTimeNanos60s50thPercentileLatency', '')],
        [('DataNode', 'PacketAckRoundTripTimeNanos60s75thPercentileLatency', '')],
        [('DataNode', 'PacketAckRoundTripTimeNanos60s90thPercentileLatency', '')],
        [('DataNode', 'PacketAckRoundTripTimeNanos60s95thPercentileLatency', '')],
        [('DataNode', 'PacketAckRoundTripTimeNanos60s99thPercentileLatency', '')],
        [('DataNode', 'PacketAckRoundTripTimeNanos300sNumOps', '')],
        [('DataNode', 'PacketAckRoundTripTimeNanos300s50thPercentileLatency', '')],
        [('DataNode', 'PacketAckRoundTripTimeNanos300s75thPercentileLatency', '')],
        [('DataNode', 'PacketAckRoundTripTimeNanos300s90thPercentileLatency', '')],
        [('DataNode', 'PacketAckRoundTripTimeNanos300s95thPercentileLatency', '')],
        [('DataNode', 'PacketAckRoundTripTimeNanos300s99thPercentileLatency', '')],
        [('DataNode', 'PacketAckRoundTripTimeNanos900sNumOps', '')],
        [('DataNode', 'PacketAckRoundTripTimeNanos900s50thPercentileLatency', '')],
        [('DataNode', 'PacketAckRoundTripTimeNanos900s75thPercentileLatency', '')],
        [('DataNode', 'PacketAckRoundTripTimeNanos900s90thPercentileLatency', '')],
        [('DataNode', 'PacketAckRoundTripTimeNanos900s95thPercentileLatency', '')],
        [('DataNode', 'PacketAckRoundTripTimeNanos900s99thPercentileLatency', '')],
        [('DataNode', 'FlushNanos60sNumOps', '')],
        [('DataNode', 'FlushNanos60s50thPercentileLatency', '')],
        [('DataNode', 'FlushNanos60s75thPercentileLatency', '')],
        [('DataNode', 'FlushNanos60s90thPercentileLatency', '')],
        [('DataNode', 'FlushNanos60s95thPercentileLatency', '')],
        [('DataNode', 'FlushNanos60s99thPercentileLatency', '')],
        [('DataNode', 'FlushNanos300sNumOps', '')],
        [('DataNode', 'FlushNanos300s50thPercentileLatency', '')],
        [('DataNode', 'FlushNanos300s75thPercentileLatency', '')],
        [('DataNode', 'FlushNanos300s90thPercentileLatency', '')],
        [('DataNode', 'FlushNanos300s95thPercentileLatency', '')],
        [('DataNode', 'FlushNanos300s99thPercentileLatency', '')],
        [('DataNode', 'FlushNanos900sNumOps', '')],
        [('DataNode', 'FlushNanos900s50thPercentileLatency', '')],
        [('DataNode', 'FlushNanos900s75thPercentileLatency', '')],
        [('DataNode', 'FlushNanos900s90thPercentileLatency', '')],
        [('DataNode', 'FlushNanos900s95thPercentileLatency', '')],
        [('DataNode', 'FlushNanos900s99thPercentileLatency', '')],
        [('DataNode', 'FsyncNanos60sNumOps', '')],
        [('DataNode', 'FsyncNanos60s50thPercentileLatency', '')],
        [('DataNode', 'FsyncNanos60s75thPercentileLatency', '')],
        [('DataNode', 'FsyncNanos60s90thPercentileLatency', '')],
        [('DataNode', 'FsyncNanos60s95thPercentileLatency', '')],
        [('DataNode', 'FsyncNanos60s99thPercentileLatency', '')],
        [('DataNode', 'FsyncNanos300sNumOps', '')],
        [('DataNode', 'FsyncNanos300s50thPercentileLatency', '')],
        [('DataNode', 'FsyncNanos300s75thPercentileLatency', '')],
        [('DataNode', 'FsyncNanos300s90thPercentileLatency', '')],
        [('DataNode', 'FsyncNanos300s95thPercentileLatency', '')],
        [('DataNode', 'FsyncNanos300s99thPercentileLatency', '')],
        [('DataNode', 'FsyncNanos900sNumOps', '')],
        [('DataNode', 'FsyncNanos900s50thPercentileLatency', '')],
        [('DataNode', 'FsyncNanos900s75thPercentileLatency', '')],
        [('DataNode', 'FsyncNanos900s90thPercentileLatency', '')],
        [('DataNode', 'FsyncNanos900s95thPercentileLatency', '')],
        [('DataNode', 'FsyncNanos900s99thPercentileLatency', '')],
        [('DataNode', 'SendDataPacketBlockedOnNetworkNanos60sNumOps', '')],
        [('DataNode', 'SendDataPacketBlockedOnNetworkNanos60s50thPercentileLatency', '')],
        [('DataNode', 'SendDataPacketBlockedOnNetworkNanos60s75thPercentileLatency', '')],
        [('DataNode', 'SendDataPacketBlockedOnNetworkNanos60s90thPercentileLatency', '')],
        [('DataNode', 'SendDataPacketBlockedOnNetworkNanos60s95thPercentileLatency', '')],
        [('DataNode', 'SendDataPacketBlockedOnNetworkNanos60s99thPercentileLatency', '')],
        [('DataNode', 'SendDataPacketBlockedOnNetworkNanos300sNumOps', '')],
        [('DataNode', 'SendDataPacketBlockedOnNetworkNanos300s50thPercentileLatency', '')],
        [('DataNode', 'SendDataPacketBlockedOnNetworkNanos300s75thPercentileLatency', '')],
        [('DataNode', 'SendDataPacketBlockedOnNetworkNanos300s90thPercentileLatency', '')],
        [('DataNode', 'SendDataPacketBlockedOnNetworkNanos300s95thPercentileLatency', '')],
        [('DataNode', 'SendDataPacketBlockedOnNetworkNanos300s99thPercentileLatency', '')],
        [('DataNode', 'SendDataPacketBlockedOnNetworkNanos900sNumOps', '')],
        [('DataNode', 'SendDataPacketBlockedOnNetworkNanos900s50thPercentileLatency', '')],
        [('DataNode', 'SendDataPacketBlockedOnNetworkNanos900s75thPercentileLatency', '')],
        [('DataNode', 'SendDataPacketBlockedOnNetworkNanos900s90thPercentileLatency', '')],
        [('DataNode', 'SendDataPacketBlockedOnNetworkNanos900s95thPercentileLatency', '')],
        [('DataNode', 'SendDataPacketBlockedOnNetworkNanos900s99thPercentileLatency', '')],
        [('DataNode', 'SendDataPacketTransferNanos60sNumOps', '')],
        [('DataNode', 'SendDataPacketTransferNanos60s50thPercentileLatency', '')],
        [('DataNode', 'SendDataPacketTransferNanos60s75thPercentileLatency', '')],
        [('DataNode', 'SendDataPacketTransferNanos60s90thPercentileLatency', '')],
        [('DataNode', 'SendDataPacketTransferNanos60s95thPercentileLatency', '')],
        [('DataNode', 'SendDataPacketTransferNanos60s99thPercentileLatency', '')],
        [('DataNode', 'SendDataPacketTransferNanos300sNumOps', '')],
        [('DataNode', 'SendDataPacketTransferNanos300s50thPercentileLatency', '')],
        [('DataNode', 'SendDataPacketTransferNanos300s75thPercentileLatency', '')],
        [('DataNode', 'SendDataPacketTransferNanos300s90thPercentileLatency', '')],
        [('DataNode', 'SendDataPacketTransferNanos300s95thPercentileLatency', '')],
        [('DataNode', 'SendDataPacketTransferNanos300s99thPercentileLatency', '')],
        [('DataNode', 'SendDataPacketTransferNanos900sNumOps', '')],
        [('DataNode', 'SendDataPacketTransferNanos900s50thPercentileLatency', '')],
        [('DataNode', 'SendDataPacketTransferNanos900s75thPercentileLatency', '')],
        [('DataNode', 'SendDataPacketTransferNanos900s90thPercentileLatency', '')],
        [('DataNode', 'SendDataPacketTransferNanos900s95thPercentileLatency', '')],
        [('DataNode', 'SendDataPacketTransferNanos900s99thPercentileLatency', '')],
      ]),
    ],
  },
  'hbase' : {
    'master':[
      ('Operation', [
        [('HBase', 'putNumOps', 'op(s)')],
        [('HBase', 'putAvgTime', 'us(s)')],
        [('HBase', 'checkAndPutNumOps', 'op(s)')],
        [('HBase', 'checkAndPutAvgTime', 'us(s)')],
        [('HBase', 'getNumOps', 'op(s)')],
        [('HBase', 'getAvgTime', 'us(s)')],
        [('HBase', 'deleteNumOps', 'op(s)')],
        [('HBase', 'deleteAvgTime', 'us(s)')],
      ]),
      ('RPC', [
        [('HBase', 'RpcQueueTimeNumOps', 'op(s)')],
        [('HBase', 'RpcQueueTimeAvgTime', 'ms(s)')],
        [('HBase', 'RpcProcessingTimeNumOps', 'op(s)')],
        [('HBase', 'RpcProcessingTimeAvgTime', 'us(s)')],
        [('HBase', 'RpcSlowResponseNumOps', 'op(s)')],
        [('HBase', 'RpcSlowResponseAvgTime', 'ms(s)')],
      ]),
      ('JvmStatistics', [
        [('Master', 'memHeapCommittedM', 'MB')],
        [('Master', 'fatalCount', 'count(s)')],
        [('Master', 'threadsWaiting', 'thread(s)')],
        [('Master', 'threadsBlocked', 'thread(s)')],
        [('Master', 'gcCount', 'count(s)')],
        [('Master', 'errorCount', 'count(s)')],
        [('Master', 'memNonHeapCommittedM', 'MB')],
        [('Master', 'warnCount', 'count(s)')],
        [('Master', 'gcTimeMillis', 'ms(s)')],
        [('Master', 'memNonHeapUsedM', 'MB')],
        [('Master', 'memHeapUsedM', 'MB')],
        [('Master', 'threadsNew', 'thread(s)')],
        [('Master', 'threadsTerminated', 'thread(s)')],
        [('Master', 'threadsTimedWaiting', 'thread(s)')],
        [('Master', 'maxMemoryM', 'MB')],
        [('Master', 'infoCount', 'count(s)')],
        [('Master', 'threadsRunnable', 'thread(s)')],
      ]),
    ],
    'regionserver': [
      ('Operation', [
        [('HBase', 'multiNumOps', 'op(s)')],
        [('HBase', 'multiAvgTime', 'us(s)')],
        [('HBase', 'checkAndPutNumOps', 'op(s)')],
        [('HBase', 'checkAndPutAvgTime', 'us(s)')],
        [('HBase', 'getNumOps', 'op(s)')],
        [('HBase', 'getAvgTime', 'us(s)')],
        [('HBase', 'openScannerNumOps', 'op(s)')],
        [('HBase', 'openScannerAvgTime', 'us(s)')],
        [('HBase', 'nextNumOps', 'op(s)')],
        [('HBase', 'nextAvgTime', 'us(s)')],
        [('HBase', 'deleteNumOps', 'op(s)')],
        [('HBase', 'deleteAvgTime', 'us(s)')],
      ]),
      ('RPC', [
        [('HBase', 'RpcQueueTimeNumOps', 'op(s)')],
        [('HBase', 'RpcQueueTimeAvgTime', 'ms(s)')],
        [('HBase', 'RpcProcessingTimeNumOps', 'op(s)')],
        [('HBase', 'RpcProcessingTimeAvgTime', 'us(s)')],
        [('HBase', 'RpcSlowResponseNumOps', 'op(s)')],
        [('HBase', 'RpcSlowResponseAvgTime', 'ms(s)')],
      ]),
      ('Store', [
        [('RegionServer', 'regions', 'region(s)')],
        [('RegionServer', 'memstoreSizeMB', 'MB')],
        [('RegionServer', 'storefileIndexSizeMB', 'MB')],
        [('RegionServer', 'storeFileSizeMB', 'MB')],
        [('RegionServer', 'storefiles', 'file(s)')],
        [('RegionServer', 'stores', 'store(s)')],
        [('RegionServer', 'largeCompactionQueueSize', 'count(s)')],
        [('RegionServer', 'smallCompactionQueueSize', 'count(s)')],
        [('RegionServer', 'compactionTime', 'ms(s)')],
        [('RegionServer', 'compactionSize', 'byte(s)')],
        [('RegionServer', 'flushQueueSize', 'count(s)')],
        [('RegionServer', 'flushTime', 'second(s)')],
        [('RegionServer', 'flushSize', 'byte(s)')],
        [('RegionServer', 'hlogRollCount', 'count(s)')],
      ]),
      ('BlockCache', [
        [('RegionServer', 'blockCacheCount', 'count(s)')],
        [('RegionServer', 'blockCacheFree', 'byte(s)')],
        [('RegionServer', 'blockCacheHitRatio', '%')],
        [('RegionServer', 'blockCacheHitCount', 'count(s)')],
        [('RegionServer', 'blockCacheMissCount', 'count(s)')],
        [('RegionServer', 'blockCacheSize', 'byte(s)' )],
      ]),
      ('Replication', [
        [('Replication', 'sizeOfLogQueue-5', '')],
        [('Replication', 'ageOfLastShippedOp-5', '')],
        [('Replication', 'logEditsReadRate-5', '')],
        [('Replication', 'shippedOpsRate-5', '')],
        [('Replication', 'logEditsFilteredRate-5', '')],
        [('Replication', 'shippedBatchesRate-5', '')],
      ]),
      ('FileSystem', [
        [('RegionServer', 'fsReadLatencyNumOps', 'op(s)')],
        [('RegionServer', 'fsReadLatencyAvgTime', 'ms(s)')],
        [('RegionServer', 'fsPreadLatencyNumOps', 'op(s)')],
        [('RegionServer', 'fsPreadLatencyAvgTime', 'ms(s)')],
        [('RegionServer', 'fsWriteLatencyNumOps', 'op(s)')],
        [('RegionServer', 'fsWriteLatencyAvgTime', 'ms(s)')],
        [('RegionServer', 'fsSyncLatencyNumOps', 'op(s)')],
        [('RegionServer', 'fsSyncLatencyAvgTime', 'ms(s)')],
      ]),
      ('JvmStatistics', [
        [('RegionServer', 'memHeapCommittedM', 'MB')],
        [('RegionServer', 'fatalCount', 'count(s)')],
        [('RegionServer', 'threadsWaiting', 'thread(s)')],
        [('RegionServer', 'threadsBlocked', 'thread(s)')],
        [('RegionServer', 'gcCount', 'count(s)')],
        [('RegionServer', 'errorCount', 'count(s)')],
        [('RegionServer', 'memNonHeapCommittedM', 'MB')],
        [('RegionServer', 'warnCount', 'count(s)')],
        [('RegionServer', 'gcTimeMillis', 'ms(s)')],
        [('RegionServer', 'memNonHeapUsedM', 'MB')],
        [('RegionServer', 'memHeapUsedM', 'MB')],
        [('RegionServer', 'threadsNew', 'thread(s)')],
        [('RegionServer', 'threadsTerminated', 'thread(s)')],
        [('RegionServer', 'threadsTimedWaiting', 'thread(s)')],
        [('RegionServer', 'maxMemoryM', 'MB')],
        [('RegionServer', 'infoCount', 'count(s)')],
        [('RegionServer', 'threadsRunnable', 'thread(s)')],
      ]),
    ],
  }
}

REGION_SERVER_OPERATION_VIEW_CONFIG = ['multi', 'get', 'openScanner', 'next',
                                       'delete', 'checkAndPut', 'execCoprocessor']
REPLICATION_METRICS_VIEW_CONFIG = ['sizeOfLogQueue', 'ageOfLastShippedOp', 'logEditsReadRate',
                                   'shippedOpsRate', 'logEditsFilteredRate', 'shippedBatchesRate',
                                   'logReadRateInByte']
