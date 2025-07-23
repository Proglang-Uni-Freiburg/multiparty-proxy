from wf_checker import check_well_formedness, project_protocol

try:
    check_well_formedness(r"C:\Tools\myPythonScrib\temp_scribble_tool\scribble-python\test\popl14\Negotiation1.scr")
    print("✅ Well-formed and reachable!")

    # full projection
    project_protocol(
        scr_path="test/popl14/Negotiation1.scr",
        full_global="popl14.Negotiation1.Negotiate",
        role="Consumer",
        output_dir="output"
    )
    print("✅ Protocol projected")
except Exception as e:
    print("❌ Invalid protocol:", e)