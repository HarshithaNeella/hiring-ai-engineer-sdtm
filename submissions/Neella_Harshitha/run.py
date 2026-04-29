
from preprocess import load_data, preprocess_data
from agent import infer_mapping
from tool_wrapper import generate_r_script, run_r_script
from validator import validate_output

def main():
    print("Loading data...")
    df = load_data("data/vs_raw.csv")
    df = preprocess_data(df)

    print("Agent analyzing columns...")
    mapping = infer_mapping(df)

    print("Mapping decided:")
    for m in mapping:
        print(m)

    print("Generating R script...")
    script_path = "convert.R"
    generate_r_script(mapping, script_path)

    print("Executing tool (sdtm.oak)...")
    run_r_script(script_path)

    print("Validating output...")
    validate_output("output/vs.csv", "data/vs_golden.csv")

    print("Done.")

if __name__ == "__main__":
    main()