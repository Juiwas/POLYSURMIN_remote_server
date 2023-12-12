import itertools
import os
import subprocess
import uuid
from typing import Tuple
import numpy as np
import pandas as pd


class Swan:
    def __init__(self, path_to_swan: str = os.getcwd()):
        self._path = path_to_swan
        self._templatefile = "template.swn"
        self._inputfile = "input.swn"

        self.mx = 30
        self.my = 30
        self.xp = 0
        self.yp = 0
        self.xlen = 750
        self.ylen = 750

        x = np.linspace(self.xp, self.xlen, self.mx + 1)
        y = np.linspace(self.yp, self.ylen, self.my + 1)

        self.grid = pd.DataFrame(itertools.product(x, y), columns=["x", "y"])

    def _config(self, **params) -> Tuple[str, str]:
        templatepath = os.path.join(self._path, self._templatefile)
        with open(templatepath, "r") as file:
            template_text = file.read()

        outputfile = str(uuid.uuid4())
        filled_template_text = template_text.format(
            fname=outputfile, mx=self.mx, my=self.my, **params
        )

        inputpath = os.path.join(self._path, self._inputfile)
        with open(inputpath, "w") as file:
            file.write(filled_template_text)

        return outputfile

    def _swanrun(self) -> subprocess.Popen:
        args = ['sh',os.path.join(self._path, "swanrun"), '-input',self._inputfile[:-4]]
        return subprocess.Popen(args, cwd=self._path)

    def run(self, data: dict):
        result: pd.DataFrame = pd.DataFrame()

        for ind in data:
            # TODO обработать ошибки
            outputfile = self._config(**data[ind])
            self._swanrun().wait()

            outputpath = os.path.join(self._path, outputfile)

            if not os.path.exists(outputpath):
                continue

            hsign = np.fromfile(outputpath, sep=" ")
            os.remove(outputpath)

            df = self.grid.copy()
            df["hsign"] = hsign

            keys, values = list(data[ind].keys()), list(data[ind].values())
            df[keys] = values

            # result.append(df)
            result = pd.concat([result, df])

        self._cleanup()

        # return result.reindex(axis='index').to_dict('index')
        return result.to_dict("list")

    def _cleanup(self):
        files = [
            f"{self._inputfile[:-4]}.prt",
            self._inputfile,
            "norm_end",
            "swaninit",
        ]

        for file in files:
            path = os.path.join(self._path, file)
            if os.path.exists(path):
                os.remove(path)