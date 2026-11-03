# React2Shell local target

Next.js 16.0.6, React 19.2.0을 사용한다. 호스트의 `127.0.0.1:3000`에만 게시한다. 기본 페이지에는 `Hello, this is gl4ss!`만 표시된다.

## 실행

```sh
cd server
docker compose up --build -d
curl -i http://127.0.0.1:3000/
docker compose logs -f target
```

종료할 때는 `docker compose down`을 실행한다. 런타임은 프로젝트 전용 Docker 브리지 네트워크를 사용하며, 컨테이너에는 호스트 디렉터리나 Docker 소켓을 마운트하지 않는다.

## PoC

다른 터미널에서 다음 명령을 실행한다.

```sh
cd react2shell
python3 -m pip install -r requirements.txt
python3 poc.py
```

기본 타임아웃은 10초다. 서버 로그의 `91455`와 `[lab] PoC marker stack`을 확인한다. HTTP 상태만으로 실행 여부를 판정하지 않는다.

## 디버거

`compose.debug.yaml`은 같은 취약 서버를 development + Webpack 모드로 실행하고 Inspector를 `127.0.0.1:9229`에 게시한다. 실행 방법과 캡처 지점은 [../DEBUGGING.md](../DEBUGGING.md)에 정리했다. production과 development 결과를 구분해서 기록한다.

정확한 설치 버전은 `package-lock.json`에 기록돼 있다. 컨테이너에서 확인하려면 `docker compose exec target npm ls next react react-dom`을 실행한다.
