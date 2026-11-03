// Preserve the submitted PoC input while recording the server-side call stack
// when the working PoC marker executes.
const originalLog = console.log;
const marker = Number(process.env.POC_MARKER || 1234);

console.log = function (...args) {
  if (args.length === 1 && args[0] === marker) {
    originalLog.call(console, '[lab] PoC marker stack:\n' + new Error().stack);
  }
  return originalLog.apply(this, args);
};
