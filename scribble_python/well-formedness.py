from wf_checker import check_well_formedness, project_protocol

try:
    check_well_formedness(r"C:\Users\andre\Documents\Uni_Freiburg\SS_25\Bachelorarbeit\multiparty-proxy\Negotiate.scr")
    print("✅ Well-formed and reachable!")

    # full projection
    project_protocol(
        scr_path=r"C:\Users\andre\Documents\Uni_Freiburg\SS_25\Bachelorarbeit\multiparty-proxy\Negotiate.scr",
        full_global="Negotiate.Negotiate",
        role="Consumer",
        output_dir="output"
    )
    print("✅ Protocol projected")
except Exception as e:
    print("❌ Invalid protocol:", e)