module.exports = [
  {
    ignores: ["./dist/*"],
  },
  {
    files: ["*.js"],
    rules: {
      semi: "error",
      "no-unused-vars": "warn",
    },
  },
];
