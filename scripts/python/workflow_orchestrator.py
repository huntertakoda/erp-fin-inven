import subprocess
import os

# helper function to run a script with error handling

def run_script(script_name):
    try:
        print(f"running {script_name}...")
        subprocess.run(["python", script_name], check=True)
        print(f"completed {script_name}")
    except FileNotFoundError:
        print(f"error: {script_name} not found. skipping.")
    except subprocess.CalledProcessError as e:
        print(f"error: {script_name} failed with error: {e}")
    except Exception as e:
        print(f"unexpected error while running {script_name}: {e}")

# general ledger workflows

def run_gl_scripts():
    print("\nstarting general ledger workflows...")
    run_script("gl_balance_calculations.py")
    run_script("gl_transaction_validations.py")
    run_script("gl_reconciliation.py")

# accounts payable workflows

def run_ap_scripts():
    print("\nstarting accounts payable workflows...")
    run_script("ap_payment_schedules.py")
    run_script("ap_overdue_analysis.py")
    run_script("ap_invoice_matching.py")

# fixed assets workflows

def run_fa_scripts():
    print("\nstarting fixed assets workflows...")
    run_script("fa_depreciation_calculations.py")
    run_script("fa_lifecycle_tracking.py")
    run_script("fa_capex_analysis.py")

# inventory management workflows

def run_im_scripts():
    print("\nstarting inventory management workflows...")
    run_script("im_stock_level_updates.py")
    run_script("im_reorder_predictions.py")
    run_script("im_demand_forecasting.py")

# main workflow orchestrator

if __name__ == "__main__":
    print("initializing workflow orchestrator...\n")

    # check if scripts are in the current directory
    
    missing_scripts = []
    required_scripts = [
        "gl_balance_calculations.py",
        "gl_transaction_validations.py",
        "gl_reconciliation.py",
        "ap_payment_schedules.py",
        "ap_overdue_analysis.py",
        "ap_invoice_matching.py",
        "fa_depreciation_calculations.py",
        "fa_lifecycle_tracking.py",
        "fa_capex_analysis.py",
        "im_stock_level_updates.py",
        "im_reorder_predictions.py",
        "im_demand_forecasting.py"
    ]
    
    for script in required_scripts:
        if not os.path.exists(script):
            missing_scripts.append(script)

    if missing_scripts:
        print("warning: the following scripts are missing and will be skipped:")
        for script in missing_scripts:
            print(f"  - {script}")
    else:
        print("all required scripts are present.")

    # run workflows
    
    run_gl_scripts()
    run_ap_scripts()
    run_fa_scripts()
    run_im_scripts()

    print("\nworkflow orchestration complete!")
