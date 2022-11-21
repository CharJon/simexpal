
from . import common

class ForkLauncher(common.Launcher):
	def submit(self, config, run):
		if not common.lock_run(run):
			return
		common.create_run_file(run)

		print(f"Launching run {run.display_name} on local machine")
		manifest = common.compile_manifest(run)
		common.invoke_run(manifest)

