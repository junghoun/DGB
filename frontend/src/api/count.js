import { count } from "./index";

function fetchCount() {
  return count.get(`/`);
}

export { fetchCount };
