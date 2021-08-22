import { card } from "./index";

function fetchCard() {
  return card.get(`/`);
}

export { fetchCard };
