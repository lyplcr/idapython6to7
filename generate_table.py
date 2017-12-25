def load_apis():
    new_old_apis = [
        # start of changes for idc.py
        ("hasValue", "has_value"),
        ("byteValue", "byte_value"),
        ("isLoaded", "is_loaded"),
        ("isCode", "is_code"),
        ("isData", "is_data"),
        ("isTail", "is_tail"),
        ("isUnknown", "is_unknown"),
        ("isHead", "is_head"),
        ("isFlow", "is_flow"),
        ("isOff0", "is_off0"),
        ("isOff1", "is_off1"),
        ("isChar0", "is_char0"),
        ("isChar1", "is_char1"),
        ("isSeg0", "is_seg0"),
        ("isSeg1", "is_seg1"),
        ("isEnum0", "is_enum0"),
        ("isEnum1", "is_enum1"),
        ("isStroff0", "is_stroff0"),
        ("isStroff1", "is_stroff1"),
        ("isStkvar0", "is_stkvar0"),
        ("isStkvar1", "is_stkvar1"),
        ("isByte", "is_byte"),
        ("isWord", "is_word"),
        ("isTbyt", "is_tbyt"),
        ("isFloat", "is_float"),
        ("isDouble", "is_double"),
        ("isPackReal", "is_pack_real"),
        ("isStruct", "is_struct"),
        ("isAlign", "is_align"),
        ("IsFloat", "is_float"),
        ("Jump", "jump"),
        ("Wait", "wait"),
        ("Eval", "eval"),
        ("Exit", "exit"),
        ("DeleteAll", "delete_all"),
        ("MakeArray", "make_array"),
        ("OpHex", "op_hex"),
        ("OpChr", "op_chr"),
        ("OpOff", "op_off"),
        ("OpSeg", "op_seg"),
        ("OpStkvar", "op_stkvar"),
        ("SetManualInsn", "set_manual_insn"),
        ("GetManualInsn", "get_manual_insn"),
        ("PatchDbgByte", "patch_dbg_byte"),
        ("PatchByte", "patch_byte"),
        ("PatchWord", "patch_word"),
        ("PatchDword", "patch_dword"),
        ("PatchQword", "patch_qword"),
        ("AutoUnmark", "auto_unmark"),
        ("GetInputFile", "get_input_file"),
        ("GetInputFilePath", "get_input_file_path"),
        ("GetIdbPath", "get_idb_path"),
        ("Byte", "byte"),
        ("GetOriginalByte", "get_original_byte"),
        ("GetReg", "get_reg"),
        ("NextAddr", "next_addr"),
        ("PrevAddr", "prev_addr"),
        ("NextHead", "next_head"),
        ("PrevHead", "prev_head"),
        ("NextNotTail", "next_not_tail"),
        ("PrevNotTail", "prev_not_tail"),
        ("Demangle", "demangle"),
        ("GetOperandValue", "get_operand_value"),
        ("FindText", "find_text"),
        ("FindBinary", "find_binary"),
        ("_invoke_idc_setprm", "_invoke_idc_setprm"),
        ("SetProcessorType ", "set_processor_type "),
        ("SetTargetAssembler", "set_target_assembler"),
        ("Batch", "batch"),
        ("ProcessUiAction", "process_ui_action"),
        ("AskSeg", "ask_seg"),
        ("AskYN", "ask_yn"),
        ("Warning", "warning"),
        ("Refresh", "refresh"),
        ("RefreshLists", "refresh_lists"),
        ("FindSelector", "find_selector"),
        ("SetSelector", "set_selector"),
        ("DelSelector", "del_selector"),
        ("DelSeg", "del_seg"),
        ("MoveSegm", "move_segm"),
        ("SetStorageType", "set_storage_type"),
        ("FindFuncEnd", "find_func_end"),
        ("GetFrame", "get_frame"),
        ("GetFrameLvarSize", "get_frame_lvar_size"),
        ("GetFrameRegsSize", "get_frame_regs_size"),
        ("GetFrameArgsSize", "get_frame_args_size"),
        ("GetFrameSize", "get_frame_size"),
        ("GetSpd", "get_spd"),
        ("GetMinSpd", "get_min_spd"),
        ("RecalcSpd", "recalc_spd"),
        ("GetEntryOrdinal", "get_entry_ordinal"),
        ("GetEntryName", "get_entry_name"),
        ("GetNextFixupEA", "get_next_fixup_ea"),
        ("GetPrevFixupEA", "get_prev_fixup_ea"),
        ("SetFixup", "set_fixup"),
        ("DelFixup", "del_fixup"),
        ("GetStrucQty", "get_struc_qty"),
        ("GetFirstStrucIdx", "get_first_struc_idx"),
        ("GetLastStrucIdx", "get_last_struc_idx"),
        ("GetNextStrucIdx", "get_next_struc_idx"),
        ("GetPrevStrucIdx", "get_prev_struc_idx"),
        ("GetStrucIdx", "get_struc_idx"),
        ("GetStrucId", "get_struc_id"),
        ("GetStrucName", "get_struc_name"),
        ("GetStrucSize", "get_struc_size"),
        ("GetMemberQty", "get_member_qty"),
        ("GetMemberId", "get_member_id"),
        ("GetFirstMember", "get_first_member"),
        ("GetLastMember", "get_last_member"),
        ("GetMemberOffset", "get_member_offset"),
        ("GetMemberName", "get_member_name"),
        ("GetMemberSize", "get_member_size"),
        ("GetMemberFlag", "get_member_flag"),
        ("IsUnion", "is_union"),
        ("DelStruc", "del_struc"),
        ("SetStrucIdx", "set_struc_idx"),
        ("SetStrucName", "set_struc_name"),
        ("AddStrucMember", "add_struc_member"),
        ("DelStrucMember", "del_struc_member"),
        ("SetMemberName", "set_member_name"),
        ("SetMemberType", "set_member_type"),
        ("ExpandStruc", "expand_struc"),
        ("GetFchunkAttr", "get_fchunk_attr"),
        ("SetFchunkAttr", "set_fchunk_attr"),
        ("GetFchunkReferer", "get_fchunk_referer"),
        ("RemoveFchunk", "remove_fchunk"),
        ("GetEnumQty", "get_enum_qty"),
        ("GetnEnum", "getn_enum"),
        ("GetEnumIdx", "get_enum_idx"),
        ("GetEnum", "get_enum"),
        ("GetEnumName", "get_enum_name"),
        ("GetEnumCmt", "get_enum_cmt"),
        ("GetEnumSize", "get_enum_size"),
        ("GetEnumWidth", "get_enum_width"),
        ("GetEnumFlag", "get_enum_flag"),
        ("GetFirstBmask", "get_first_bmask"),
        ("GetLastBmask", "get_last_bmask"),
        ("GetNextBmask", "get_next_bmask"),
        ("GetPrevBmask", "get_prev_bmask"),
        ("GetBmaskName", "get_bmask_name"),
        ("GetBmaskCmt", "get_bmask_cmt"),
        ("SetBmaskName", "set_bmask_name"),
        ("SetBmaskCmt", "set_bmask_cmt"),
        ("AddEnum", "add_enum"),
        ("DelEnum", "del_enum"),
        ("SetEnumIdx", "set_enum_idx"),
        ("SetEnumName", "set_enum_name"),
        ("SetEnumCmt", "set_enum_cmt"),
        ("SetEnumFlag", "set_enum_flag"),
        ("SetEnumBf", "set_enum_bf"),
        ("SetEnumWidth", "set_enum_width"),
        ("CreateArray", "create_array"),
        ("GetArrayId", "get_array_id"),
        ("RenameArray", "rename_array"),
        ("DeleteArray", "delete_array"),
        ("SetArrayLong", "set_array_long"),
        ("SetArrayString", "set_array_string"),
        ("GetArrayElement", "get_array_element"),
        ("DelArrayElement", "del_array_element"),
        ("GetFirstIndex", "get_first_index"),
        ("GetLastIndex", "get_last_index"),
        ("GetNextIndex", "get_next_index"),
        ("GetPrevIndex", "get_prev_index"),
        ("SetHashLong", "set_hash_long"),
        ("GetHashLong", "get_hash_long"),
        ("SetHashString", "set_hash_string"),
        ("GetHashString", "get_hash_string"),
        ("GetFirstHashKey", "get_first_hash_key"),
        ("GetLastHashKey", "get_last_hash_key"),
        ("GetNextHashKey", "get_next_hash_key"),
        ("GetPrevHashKey", "get_prev_hash_key"),
        ("GetType", "get_type"),
        ("GetTinfo", "get_tinfo"),
        ("GetLocalTinfo", "get_local_tinfo"),
        ("GuessType", "guess_type"),
        ("ApplyType", "apply_type"),
        ("SetLocalType", "set_local_type"),
        ("LoadDebugger", "load_debugger"),
        ("AttachProcess", "attach_process"),
        ("DetachProcess", "detach_process"),
        ("GetThreadQty", "get_thread_qty"),
        ("SelectThread", "select_thread"),
        ("SuspendThread", "suspend_thread"),
        ("ResumeThread", "resume_thread"),
        ("GetFirstModule", "get_first_module"),
        ("GetNextModule", "get_next_module"),
        ("GetModuleName", "get_module_name"),
        ("GetModuleSize", "get_module_size"),
        ("StepInto", "step_into"),
        ("StepOver", "step_over"),
        ("RunTo", "run_to"),
        ("StepUntilRet", "step_until_ret"),
        ("GetDebuggerEvent", "get_debugger_event"),
        ("ResumeProcess", "resume_process"),
        ("SendDbgCommand", "send_dbg_command"),
        ("RefreshDebuggerMemory", "refresh_debugger_memory"),
        ("TakeMemorySnapshot", "take_memory_snapshot"),
        ("GetProcessState", "get_process_state"),
        ("GetEventId", "get_event_id"),
        ("GetEventPid", "get_event_pid"),
        ("GetEventTid", "get_event_tid"),
        ("GetEventEa", "get_event_ea"),
        ("IsEventHandled", "is_event_handled"),
        ("GetEventModuleName", "get_event_module_name"),
        ("GetEventModuleBase", "get_event_module_base"),
        ("GetEventModuleSize", "get_event_module_size"),
        ("GetEventExitCode", "get_event_exit_code"),
        ("GetEventInfo", "get_event_info"),
        ("SetDebuggerOptions", "set_debugger_options"),
        ("SetRemoteDebugger", "set_remote_debugger"),
        ("DefineException", "define_exception"),
        ("GetRegValue", "get_reg_value"),
        ("SetRegValue", "set_reg_value"),
        ("GetBptQty", "get_bpt_qty"),
        ("GetBptEA", "get_bpt_ea"),
        ("GetBptAttr", "get_bpt_attr"),
        ("SetBptAttr", "set_bpt_attr"),
        ("AddBpt", "add_bpt"),
        ("DelBpt", "del_bpt"),
        ("EnableBpt", "enable_bpt"),
        ("CheckBpt", "check_bpt"),
        ("EnableTracing", "enable_tracing"),
        ("GetStepTraceOptions", "get_step_trace_options"),
        ("SetStepTraceOptions", "set_step_trace_options"),
        ("LoadTraceFile", "load_trace_file"),
        ("SaveTraceFile", "save_trace_file"),
        ("DiffTraceFile", "diff_trace_file"),
        ("GetTevEa", "get_tev_ea"),
        ("GetTevType", "get_tev_type"),
        ("GetTevTid", "get_tev_tid"),
        ("GetBptTevEa", "get_bpt_tev_ea"),
        ("GetColor", "get_color"),
        ("SetColor", "set_color"),
        ("OpOffset", "op_offset"),
        ("OpNum", "op_num"),
        ("OpDec", "op_dec"),
        ("set_start_cs", "set_start_cs"),
        ("set_start_ip", "set_start_ip"),
        ("BeginTypeUpdating", "begin_type_updating"),
        ("EndTypeUpdating", "end_type_updating"),
        ("AddStruc", "add_struc"),
        ("OpStroff", "op_stroff"),
        ("OpEnum", "op_enum"),
        ("SetReg", "set_reg"),
        ("here", "here"),
        ("isVar", None),
        ("isDefArg0", "is_defarg0"),
        ("isDefArg1", "is_defarg1"),
        ("isFop0", "is_manual0"),
        ("isFop1", "is_manual1"),
        ("FF_DWRD", "FF_DWORD"),
        ("FF_QWRD", "FF_QWORD"),
        ("FF_TBYT", "FF_TBYTE"),
        ("FF_ASCI", "FF_STRLIT"),
        ("FF_STRU", "FF_STRUCT"),
        ("FF_OWRD", "FF_OWORD"),
        ("isDwrd", "is_dword"),
        ("isQwrd", "is_qword"),
        ("isOwrd", "is_oword"),
        ("isASCII", "is_strlit"),
        ("IsString", "value_is_string"),
        ("IsLong", "value_is_long"),
        ("IsFunc", "value_is_func"),
        (None, "value_is_float"),
        ("IsPvoid", "value_is_pvoid"),
        ("IsInt64", "value_is_int64"),
        ("MK_FP", "to_ea"),
        ("AddHotkey", "add_idc_hotkey"),
        ("DelHotkey", "del_idc_hotkey"),
        (None, "auto_wait"),
        ("CompileEx", None),
        ("SaveBase", "save_database"),
        ("ValidateNames", "validate_idb_names"),
        ("Exit", "qexit"),
        ("Sleep", "qsleep"),
        ("RunPlugin", "load_and_run_plugin"),
        ("ApplySig", "plan_to_apply_idasgn"),
        ("MakeCode", "create_insn"),
        ("AnalyzeArea", "plan_and_wait"),
        ("MakeNameEx", "set_name"),
        ("MakeComm", "set_cmt"),
        ("MakeRptCmt", None),
        ("MakeStr", "create_strlit"),
        ("MakeData", "create_data"),
        ("MakeByte", "create_byte"),
        ("MakeWord", "create_word"),
        ("MakeDword", "create_dword"),
        ("MakeQword", "create_qword"),
        ("MakeOword", "create_oword"),
        ("MakeYword", "create_yword"),
        ("MakeFloat", "create_float"),
        ("MakeDouble", "create_double"),
        ("MakePackReal", "create_pack_real"),
        ("MakeTbyte", "create_tbyte"),
        ("MakeStructEx", "create_struct"),
        ("MakeCustomDataEx", "create_custom_data"),
        ("MakeAlign", "create_align"),
        ("MakeLocal", "define_local_var"),
        ("MakeUnkn", None),
        ("MakeUnknown", "del_items"),
        ("DOUNK_SIMPLE", "DELIT_SIMPLE"),
        ("DOUNK_EXPAND", "DELIT_EXPAND"),
        ("SetArrayFormat", "set_array_params"),
        ("OpBinary", "op_bin"),
        ("OpOctal", "op_oct"),
        ("OpDecimal", None),
        (None, "op_plain_offset"),
        ("OpOffEx", None),
        ("OpNumber", None),
        ("OpFloat", "op_flt"),
        ("OpAlt", "op_man"),
        ("OpSign", "toggle_sign"),
        ("OpNot", "toggle_bnot"),
        ("OpEnumEx", None),
        ("OpStroffEx", None),
        ("OpHigh", "op_offset_high16"),
        (None, "E_PREV"),
        (None, "E_NEXT"),
        ("ExtLinA", "get_extra_cmt"),
        ("ExtLinB", "update_extra_cmt"),
        ("DelExtLnA", None),
        ("DelExtLnB", "del_extra_cmt"),
        ("SetFlags", None),
        ("SetRegEx", "split_sreg_range"),
        ("AutoMark", "auto_unmark"),
        ("GenerateFile", "gen_file"),
        ("GenFuncGdl", "gen_flow_graph"),
        ("GenCallGdl", "gen_simple_call_chart"),
        ("GetIdaDirectory", "idadir"),
        ("SetInputFilePath", "set_root_filename"),
        ("GetInputMD5", "retrieve_input_file_md5"),
        ("GetFlags", "get_full_flags"),
        ("IdbByte", "get_db_byte"),
        ("GetManyBytes", "get_bytes"),
        ("DbgByte", "read_dbg_byte"),
        ("DbgWord", "read_dbg_word"),
        ("DbgDword", "read_dbg_dword"),
        ("DbgQword", "read_dbg_qword"),
        ("DbgRead", "read_dbg_memory"),
        ("DbgWrite", "write_dbg_memory"),
        ("Word", "get_wide_word"),
        ("Dword", "get_wide_dword"),
        ("Qword", "get_qword"),
        ("LocByName", "get_name_ea_simple"),
        ("LocByNameEx", "get_name_ea"),
        ("SegByBase", "get_segm_by_sel"),
        ("ScreenEA", "get_screen_ea"),
        ("GetCurrentLine", "get_curline"),
        ("SelStart", "read_selection_start"),
        ("SelEnd", "read_selection_end"),
        (None, "get_sreg"),
        ("ItemHead", "get_item_head"),
        ("ItemEnd", "get_item_end"),
        ("ItemSize", "get_item_end"),
        ("NameEx", "func_contains"),
        ("GetTrueNameEx", None),
        ("GetDisasmEx", "generate_disasm_line"),
        ("GetMnem", "print_insn_mnem"),
        ("GetOpnd", "print_operand"),
        ("GetOpType", "get_operand_type"),
        ("LineA", None),
        ("LineB", None),
        ("CommentEx", "get_cmt"),
        ("AltOp", "get_forced_operand"),
        ("GetString", "get_strlit_contents"),
        ("GetStringType", "get_str_type"),
        ("FindVoid", "find_suspop"),
        ("FindCode", "find_code"),
        ("FindData", "find_data"),
        ("FindUnexplored", "find_unknown"),
        ("FindExplored", "find_defined"),
        ("FindImmediate", "find_imm"),
        ("ChangeConfig", "process_config_line"),
        ("GetLongPrm", "get_inf_attr"),
        ("GetShortPrm", None),
        ("GetCharPrm ", None),
        ("SetLongPrm ", None),
        ("SetShortPrm", None),
        ("SetCharPrm ", None),
        ("SetPrcsr", None),
        ("AskStr", None),
        ("AskFile", None),
        ("AskAddr", None),
        ("AskLong", None),
        ("AskIdent", None),
        ("Message", None),
        ("UMessage", "msg"),
        ("Fatal", "error"),
        ("SetStatus", "set_ida_state"),
        ("AskSelector", "sel2para"),
        ("FirstSeg", "get_first_seg"),
        ("NextSeg", "get_next_seg"),
        ("SegStart", "get_segm_start"),
        ("SegEnd", "get_segm_end"),
        ("SegName", "get_segm_name"),
        ("AddSegEx", "add_segm_ex"),
        ("SetSegBounds", "set_segment_bounds"),
        ("RenameSeg", "set_segm_name"),
        ("SetSegClass", "set_segm_class"),
        ("SegAlign", "set_segm_alignment"),
        ("SegComb", "set_segm_combination"),
        ("SetSegAddressing", "set_segm_addressing"),
        ("SegByName", "selector_by_name"),
        ("SetSegDefReg", "set_default_sreg_value"),
        ("SetSegmentType", "set_segm_type"),
        ("GetSegmentAttr", "get_segm_attr"),
        ("SetSegmentAttr", "set_segm_attr"),
        ("AddCodeXref", "add_cref"),
        ("DelCodeXref", "del_cref"),
        ("Rfirst", "get_first_cref_from"),
        ("Rnext", "get_next_cref_from"),
        ("RfirstB", "get_first_cref_to"),
        ("RnextB", "get_next_cref_to"),
        ("Rfirst0", "get_first_fcref_from"),
        ("Rnext0", "get_next_fcref_from"),
        ("RfirstB0", "get_first_fcref_to"),
        ("RnextB0", "get_next_fcref_to"),
        ("Dfirst", "get_first_dref_from"),
        ("Dnext", "get_next_dref_from"),
        ("DfirstB", "get_first_dref_to"),
        ("DnextB", "get_next_dref_to"),
        ("XrefType", "get_xref_type"),
        ("MakeFunction", "add_func"),
        ("DelFunction", "del_func"),
        ("SetFunctionEnd", "set_func_end"),
        ("NextFunction", "get_next_func"),
        ("PrevFunction", "get_prev_func"),
        ("GetFunctionAttr", "get_func_attr"),
        ("SetFunctionAttr", "set_func_attr"),
        ("GetFunctionFlags", "get_func_flags"),
        ("SetFunctionFlags", "set_func_flags"),
        ("GetFunctionName", "get_func_name"),
        ("GetFunctionCmt", "get_func_cmt"),
        ("SetFunctionCmt", "set_func_cmt"),
        ("ChooseFunction", "choose_func"),
        ("GetFuncOffset", "get_func_off_str"),
        ("MakeFrame", "set_frame_size"),
        ("GetSpDiff", "get_sp_delta"),
        ("SetSpDiff", None),
        ("AddAutoStkPnt2", "add_auto_stkpnt"),
        ("AddUserStkPnt", "add_user_stkpnt"),
        ("DelStkPnt", "del_stkpnt"),
        ("GetEntryPointQty", "get_entry_qty"),
        ("AddEntryPoint", "add_entry"),
        ("GetEntryPoint", "get_entry_qty"),
        ("RenameEntryPoint", "rename_entry"),
        ("GetFixupTgtType", "get_fixup_target_type"),
        ("GetFixupTgtSel", None),
        ("GetFixupTgtOff", "get_fixup_target_off"),
        ("GetFixupTgtDispl", "get_fixup_target_dis"),
        ("MarkPosition", "put_bookmark"),
        ("GetMarkedPos", "get_bookmark"),
        ("GetMarkComment", "get_bookmark_desc"),
        ("GetStrucIdByName", "get_struc_id"),
        ("GetStrucComment", "get_struc_cmt"),
        ("GetStrucPrevOff", "get_prev_offset"),
        ("GetStrucNextOff", "get_next_offset"),
        ("GetMemberComment", "get_member_cmt"),
        ("GetMemberStrId", "get_member_strid"),
        ("AddStrucEx", "add_struc"),
        ("SetStrucComment", "set_struc_cmt"),
        ("SetMemberComment", "set_member_cmt"),
        ("NextFchunk", "get_next_fchunk"),
        ("PrevFchunk", "get_prev_fchunk"),
        ("AppendFchunk", "append_func_tail"),
        ("SetFchunkOwner", "set_tail_owner"),
        ("FirstFuncFchunk", "first_func_chunk"),
        ("NextFuncFchunk", "next_func_chunk"),
        (None, "get_enum"),
        ("GetConstByName", "get_enum_member_by_name"),
        ("GetConstValue", "get_enum_member_value"),
        ("GetConstBmask", "get_enum_member_bmask"),
        ("GetConstEnum", "get_enum_member_enum"),
        ("GetConstEx", "get_enum_member"),
        ("GetFirstConst", "get_first_enum_member"),
        ("GetLastConst", "get_last_enum_member"),
        ("GetNextConst", "get_next_enum_member"),
        ("GetPrevConst", "get_prev_enum_member"),
        ("GetConstName", "get_enum_member_name"),
        ("GetConstCmt", "get_enum_member_cmt"),
        ("IsBitfield", "is_bf"),
        ("AddConstEx", "add_enum_member"),
        ("DelConstEx", "del_enum_member"),
        ("SetConstName", "set_enum_member_name"),
        ("SetConstCmt", "set_enum_member_cmt"),
        ("DelHashElement", "del_hash_string"),
        ("AddSourceFile", "add_sourcefile"),
        ("GetSourceFile", "get_sourcefile"),
        ("DelSourceFile", "del_sourcefile"),
        ("SetLineNumber", "set_source_linnum"),
        ("GetLineNumber", "get_source_linnum"),
        ("DelLineNumber", "del_source_linnum"),
        ("LoadTil", "add_default_til"),
        ("Til2Idb", "import_type"),
        ("ParseType", "parse_decl"),
        ("ParseTypes", "parse_decls"),
        ("PrintLocalTypes", "print_decls"),
        ("GetMaxLocalType", "get_ordinal_qty"),
        ("GetLocalTypeName", "get_numbered_type_name"),
        ("HideArea", "add_hidden_range"),
        ("SetHiddenArea", "update_hidden_range"),
        ("DelHiddenArea", "del_hidden_range"),
        ("StartDebugger", "start_process"),
        ("StopDebugger", None),
        ("PauseProcess", "suspend_process"),
        ("GetProcessQty", None),
        ("GetProcessPid", None),
        ("GetProcessName", None),
        ("GetThreadId", None),
        ("GetCurrentThreadId", None),
        ("GetEventBptHardwareEa", "get_event_bpt_hea"),
        ("GetEventExceptionCode", "get_event_exc_code"),
        ("GetEventExceptionEa", "get_event_exc_ea"),
        ("CanExceptionContinue", None),
        ("GetEventExceptionInfo", "get_event_exc_info"),
        ("GetDebuggerEventCondition", None),
        ("SetDebuggerEventCondition", "set_debugger_event_cond"),
        ("SetBptCndEx", "set_bpt_cond"),
        ("SetBptCnd", None),
        ("AddBptEx", None),
        ("CheckTraceFile", "is_valid_trace_file"),
        ("ClearTraceFile", "clear_trace"),
        ("GetTraceDesc", "get_trace_file_desc"),
        ("SetTraceDesc", "set_trace_file_desc"),
        ("GetMaxTev", "get_tev_qty"),
        ("GetTevRegVal", "get_tev_reg"),
        ("GetTevRegMemQty", "get_tev_mem_qty"),
        ("GetTevRegMem", "get_tev_mem"),
        ("GetTevRegMemEa", "get_tev_mem_ea"),
        ("GetTevCallee", "get_call_tev_callee"),
        ("GetTevReturn", "get_ret_tev_return"),
        ("ArmForceBLJump", "force_bl_jump"),
        ("ArmForceBLCall", "force_bl_call"),
        ("Compile", None),
        ("OpChar", None),
        ("OpSegment", None),
        ("OpAlt1", None),
        ("OpAlt2", None),
        ("StringStp", None),
        ("LowVoids", None),
        ("HighVoids", None),
        ("TailDepth", None),
        ("Analysis", None),
        ("Tabs", None),
        ("Voids", None),
        ("XrefShow", None),
        ("Indent", None),
        ("CmtIndent", None),
        ("AutoShow", None),
        ("MinEA", None),
        ("MaxEA", None),
        ("BeginEA", None),
        ("WriteMap", None),
        ("WriteTxt", None),
        ("WriteExe", None),
        ("AddConst", None),
        ("AddUnion", None),
        ("DelConst", None),
        ("GetConst", None),
        ("AnalyseArea", None),
        ("MakeStruct", None),
        ("MakeCustomData", None),
        ("Name", None),
        ("GetTrueName", None),
        ("MakeName", None),
        ("SegCreate", None),
        ("SegDelete", None),
        ("SegBounds", None),
        ("SegRename", None),
        ("SegClass", None),
        ("SegAddrng", None),
        ("SegDefReg", None),
        ("Comment", None),
        ("RptCmt", None),
        ("isEnabled", None),
		# update 20171224
		("AutoMark2","auto_mark_range"),
		(None, "get_wide_byte"),
		("", "calc_gtn_flags"),
		("", "o_fpreg_arm"),
		("", "o_cond"),
		("ASCSTR_C", "STRTYPE_C"),
		("ASCSTR_PASCAL", "STRTYPE_PASCAL"),
		("ASCSTR_LEN2", "STRTYPE_LEN2"),
		("ASCSTR_UNICODE", None),
		("ASCSTR_LEN4", "STRTYPE_LEN4"),
		("ASCSTR_ULEN2", None),
		("ASCSTR_ULEN4", None),
		("ASCSTR_LAST", None),
		(None, "STRTYPE_C_16"),
		(None, "STRTYPE_LEN2_16"),
		(None, "STRTYPE_LEN4_16"),
		("startEA","start_ea"),
		("endEA","end_ea"),
		(None, "get_fixup_target_flags")
s for idc.py
        ]
    return new_old_apis

api_list = load_apis()
# generate table
print "| Old           | New           |"
print "| ------------- |:-------------:|"
for old, new in api_list:
    print "| %s           | %s           |" % (old, new)
    
